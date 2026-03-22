import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ Load models
model_state = joblib.load("model_state.pkl")
intensity_model = joblib.load("model_intensity.pkl")
vectorizer = joblib.load("vectorizer.pkl")


# ✅ Home route
@app.route('/')
def home():
    return "API is running 🚀"


# ✅ Decision logic
def decide_action(state, intensity):
    if state == 'overwhelmed':
        return "box_breathing", "now"
    elif state == 'restless':
        return "grounding", "within_15_min"
    elif state == 'focused':
        return "deep_work", "now"
    elif state == 'calm':
        return "light_planning", "later_today"
    else:
        return "rest", "later_today"


# ✅ Supportive message
def generate_message(state):
    if state == 'overwhelmed':
        return "You seem overwhelmed. Take a deep breath and slow down."
    elif state == 'restless':
        return "Your mind feels active. Try grounding yourself."
    elif state == 'focused':
        return "You're in a great state to focus. Keep going!"
    elif state == 'calm':
        return "You seem calm. This is a good time to plan ahead."
    else:
        return "Take a moment to pause and reflect."


# ✅ Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')

    # Transform text
    X = vectorizer.transform([text])

    # Predictions
    state = model_state.predict(X)[0]
    intensity = int(intensity_model.predict(X)[0])

    # Confidence
    probs = model_state.predict_proba(X)
    confidence = float(probs.max())

    # Uncertainty
    uncertain_flag = 1 if confidence < 0.5 else 0

    # Decision logic with safety
    if confidence < 0.4:
        return jsonify({
            "state": state,
            "intensity": intensity,
            "confidence": confidence,
            "uncertain_flag": 1,
            "what_to_do": "pause",
            "when_to_do": "later_today",
            "message": "I'm not fully sure about your state. Let's take it slow."
        })
    else:
        action, timing = decide_action(state, intensity)

    # Message
    message = generate_message(state)

    return jsonify({
        "state": state,
        "intensity": intensity,
        "confidence": confidence,
        "uncertain_flag": uncertain_flag,
        "what_to_do": action,
        "when_to_do": timing,
        "message": message
    })


if __name__ == '__main__':
    app.run(debug=True)