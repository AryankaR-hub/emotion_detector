# Edge Deployment Plan

## On-Device Execution
The system uses Logistic Regression and TF-IDF, which are lightweight and suitable for on-device execution.

## Model Size
The trained models are small (few MB), making them easy to store on mobile devices.

## Latency
Inference is fast (<100ms), enabling real-time interaction without noticeable delay.

## Privacy
All processing happens locally, ensuring sensitive user journal data is never sent to external servers.

## Tradeoffs
- Simpler models compared to deep learning approaches
- Slight accuracy tradeoff for faster inference and lower resource usage

## Robustness

- Very short inputs ("ok", "fine") result in low confidence
- These are handled using the uncertain_flag to avoid incorrect decisions
- Missing values are handled using median (numerical) and fallback categories
- Conflicting signals reduce confidence, triggering safer recommendations