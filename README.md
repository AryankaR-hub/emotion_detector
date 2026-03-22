# 🌿 Emotional Understanding & Guidance System

## Overview
This project builds an intelligent system that understands user emotional state from journal reflections and suggests meaningful actions to guide them toward better mental states.

The system goes beyond prediction by incorporating **decision-making and uncertainty awareness**, making it suitable for real-world noisy data.

---

## 🧠 Approach

### 1. Emotional State Prediction
- Technique: **TF-IDF (unigrams + bigrams)**
- Model: **Logistic Regression**
- Reason:
  - Fast and lightweight
  - Interpretable
  - Performs well on noisy, short text

---

### 2. Intensity Prediction
- Treated as a **classification problem (1–5 levels)**
- Reason:
  - Labels are discrete and subjective
  - Classification handles noisy human labels better than regression

⚠️ Challenge:
- Weak correlation between text and intensity
- Subjective labeling leads to lower accuracy

---

### 3. Decision Engine (Core)
The system translates predictions into actionable guidance.

Examples:
- Overwhelmed → `box_breathing` (now)
- Restless → `grounding` (within 15 min)
- Focused → `deep_work` (now)
- Calm → `light_planning` (later today)

---

### 4. Uncertainty-Aware System
- Confidence is derived from prediction probabilities
- If confidence < 0.5 → `uncertain_flag = 1`

#### 🔒 Safety Layer
When confidence < 0.4:
- The system overrides decisions
- Returns a safe fallback:
  - `pause`
  - `within_15_min`

This prevents risky or incorrect recommendations under uncertainty.

---

### 5. Feature Understanding
- **Text is the dominant signal**
- Metadata (sleep, stress, energy) adds minor improvements
- Ablation study:
  - Text-only ≈ Text + Metadata

---

## 🔍 Key Insights

- Emotional data is inherently **noisy and ambiguous**
- Short inputs reduce model confidence significantly
- Overlapping emotional states create confusion
- **Uncertainty-aware systems are essential in real-world AI**

---

## 🧪 Error Analysis Summary

The model struggles with:
- Short and vague inputs ("ok", "fine")
- Ambiguous or mixed emotions
- Overlapping states (calm vs neutral, restless vs overwhelmed)

These cases highlight the limitations of purely text-based emotional understanding.

---

## ⚙️ How to Run

### 1. Setup Environment

```bash
python -m venv venv
source venv/Scripts/activate   # Windows
pip install -r requirements.txt

 
2. Run Notebooks (in order)
eda.ipynb
02_preprocessing.ipynb
03_modeling.ipynb
04_decision_engine.ipynb

Output:

data/predictions.csv
3. Run API (Bonus)
python app.py

Server runs at:

http://127.0.0.1:5000
4. Test API

Use REST Client (VS Code extension)

Create test.http:

POST http://127.0.0.1:5000/predict
Content-Type: application/json

{
  "text": "I feel overwhelmed and stressed"
}
⚠️ Common Issues
ECONNREFUSED → Ensure API is running
404 error → Use /predict endpoint (POST request)
Kernel issues → Select correct Python environment
Missing packages → Run pip install -r requirements.txt
🛡️ Robustness
Short inputs → flagged with uncertain_flag
Missing values → handled using median / fallback values
Conflicting signals → reduce confidence → safer decisions
💡 Real-World Insight

This system demonstrates that emotional understanding is inherently uncertain.

Instead of blindly predicting, the system:

Detects ambiguity
Adjusts decisions
Provides safe and meaningful guidance
🎯 Key Learning

AI systems should not only understand humans — they should guide them safely under uncertainty.

