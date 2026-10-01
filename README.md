<div align="center">
  <a href="https://youtu.be/qHt02Jnuzy4">
    <img src="https://img.youtube.com/vi/qHt02Jnuzy4/0.jpg" alt="Gemma 4 Just Got a 30ms Decision Brain! (Jeff Engine Setup)">
  </a>
  <h3>📺 <a href="https://youtu.be/qHt02Jnuzy4">Watch the full tutorial on YouTube</a></h3>
</div>

# 🧠 Jeff Gemma 30ms AI Brain

Instant local zero-shot decision brain that evaluates user speech transcripts and system states to pick actionable commands in under 30 milliseconds.

| Step 1: Input | Step 2: AI Action | Step 3: Result |
|---|---|---|
| 🎙️ User Speech / App Context | ⚡ Jeff 0.8B Single Forward Pass | 🚀 30ms Executed Command |

---

## 🌟 Key Features

- ⚡ **30ms Decision Speed**: Ultra-fast System 1 local action choice without cloud API delays.
- 🎯 **Calibrated Probabilities**: High confidence scoring (96.4% on financial & intent benchmarks).
- 🎙️ **Voice & Sensor Brain**: Map natural speech transcripts directly to 10 executable tool actions.
- 🔒 **100% Offline Autonomy**: Runs locally on Apple Silicon (MLX), NVIDIA GPUs, or multi-core CPUs.
- 📊 **254-Option Capacity**: Pick legal choices zero-shot from small Shortlists up to 254 options.

---

## 🚀 Quick Setup & Installation

Install dependencies and download the safetensors model weights directly using a single PowerShell command:

```powershell
pip install requests pyyaml huggingface-hub transformers torch ; hf download mstrasser/Jeff-Gemma4-E2B --local-dir models/Jeff-Gemma4-E2B
```

*Note: The model is run natively in-memory using standard PyTorch/Transformers pipeline to eliminate the need for complex external local servers.*

---

## 💻 Running the Decision Brain

**Run the Visual Trajectory Engine**
Execute the main script. It will automatically load the model weights, generate 8 dynamic dashboard UI states, and output the AI's step-by-step navigation trajectory:

```powershell
python main.py
```
*View the rendered live trajectory dashboard by opening `outputs/trajectory_dashboard.html` in your browser.*

---

## 📁 Repository Structure

```
Jeff Gemma/
├── main.py              # Main decision script (loads Safetensors natively via Transformers)
├── visualizer.py        # Module for SVG generation and dashboard rendering
├── README.md            # Project documentation and setup guide
├── inputs/              # UI state mock screenshots for visual demo
└── outputs/
    └── trajectory_dashboard.html  # Generated UI visual trajectory demo
```

---

## 🎯 5 Practical Use Cases

1. 🎙️ **Voice Command Router**: Convert live microphone transcripts into immediate desktop actions.
2. 🎮 **Real-Time Game Controller**: Pick optimal move choices for action games in under 30ms per turn.
3. 💬 **Customer Support Intent Switcher**: Route incoming support messages to appropriate departments.
4. 📈 **Financial Market Text Classifier**: Evaluate news headlines and market statements zero-shot.
5. 🛡️ **Safety & Moderation Guardrail**: Verify incoming user inputs against safety criteria instantly.

---

## 🔮 5 Future Enhancements

1. 🔊 **Direct Whisper Audio Integration**: Stream microphone audio straight into transcript decision loops.
2. 🌐 **Multi-Language Intent Support**: Extend zero-shot decision classification across 12 languages.
3. 🏎️ **Sub-10ms Quantized Kernels**: Optimize safetensors execution for micro-controller edge devices.
4. 🕹️ **Custom Game Environment Adapters**: Pre-built bindings for Unreal Engine and Unity agents.
5. 📊 **Live Decision Telemetry Dashboard**: Real-time visualization of confidence scores and latency.

---
**Keywords:** AI, Gemma 4, E2B, Jeff Engine, 30ms Latency, Machine Learning, Open Source AI, AI Dashboard, UI Automation, Zero-Shot Learning, Hugging Face, Transformers, Python
