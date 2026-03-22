# Error Analysis

## Case 1
Text: "lowkey felt locked in for a bit, but mountain visuals made it easier to pause."
True Label: focused
Predicted Label: restless
Confidence: 0.25

Reason:
The text contains mixed signals — "locked in" indicates focus, while "pause" suggests disengagement. The model overemphasized the latter and misclassified it as restless.

Improvement:
Using phrase-level understanding or contextual embeddings (like BERT) could help capture nuanced transitions within a sentence.

---

## Case 2
Text: "that helped a little"
True Label: calm
Predicted Label: restless
Confidence: 0.27

Reason:
The text is too short and lacks strong emotional keywords, making it ambiguous. The model defaulted to a more frequent or uncertain class.

Improvement:
Incorporating previous mood or session context could help interpret such vague reflections more accurately.

---

## Case 3
Text: "felt heavy"
True Label: calm
Predicted Label: overwhelmed
Confidence: 0.47

Reason:
The word "heavy" is often associated with stress or emotional burden, leading the model to classify it as overwhelmed, even though the true label was calm.

Improvement:
A better understanding of context or combining metadata like stress_level could help distinguish emotional weight from calmness.

---

## Case 4
Text: "got distracted again"
True Label: mixed
Predicted Label: focused
Confidence: 0.26

Reason:
The model likely picked up on "again" as a pattern of engagement, missing the negative cue "distracted," which indicates lack of focus.

Improvement:
Improved feature weighting or attention mechanisms could help emphasize negative keywords like "distracted."

---

## Case 5
Text: "i guess mind was all over the place."
True Label: focused
Predicted Label: neutral
Confidence: 0.21

Reason:
The phrase suggests mental chaos, but the model interpreted it as neutral due to lack of strong polarity words.

Improvement:
Adding domain-specific keywords (e.g., "overthinking", "scattered") could improve detection of restless or unfocused states.

---

## Case 6
Text: "... "
True Label: overwhelmed
Predicted Label: restless
Confidence: 0.33

Reason:
The model confused closely related emotional states (overwhelmed vs restless), which often share overlapping vocabulary and patterns.

Improvement:
Hierarchical classification or grouping similar emotions could reduce confusion between closely related classes.

---
## Case 7
Text: "it was okay I guess"
True Label: neutral
Predicted Label: calm
Confidence: 0.31

Reason:
The phrase is vague and lacks strong emotional indicators, making it difficult to distinguish between neutral and calm states.

Improvement:
Using sentiment intensity scoring or contextual signals like previous mood could help refine predictions.

---

## Case 8
Text: "too many thoughts at once"
True Label: overwhelmed
Predicted Label: restless
Confidence: 0.34

Reason:
Both "overwhelmed" and "restless" share similar patterns of mental activity, causing confusion in classification.

Improvement:
Incorporating metadata like stress_level or session duration could help differentiate high stress from general restlessness.

---

## Case 9
Text: "felt fine after the session"
True Label: calm
Predicted Label: neutral
Confidence: 0.42

Reason:
The word "fine" is weakly expressive and often interpreted as neutral, leading to misclassification.

Improvement:
Adding phrase-level understanding (e.g., "felt fine after") could help capture emotional transitions.

---

## Case 10
Text: "couldn't really focus much"
True Label: restless
Predicted Label: mixed
Confidence: 0.29

Reason:
The model interpreted the statement as mixed due to lack of strong polarity, while the actual signal indicates lack of focus.

Improvement:
Improving detection of negative productivity-related phrases could enhance classification of restless states.

---