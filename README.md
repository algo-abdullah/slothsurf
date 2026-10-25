# 🦥 SlothSurf — The Zero-Effort Autonomous Web Agent

> *"Slow and steady wins the race. Doing nothing wins the prize."*

Built for the **Slow and Steady (International Sloth Day)** AI Challenge.  
Powered by the open-source **`browser-use`** agent harness and **xAI Grok** (`grok-2-vision-1212`).

---

## 🌟 Overview

**SlothSurf** is an autonomous browser agent built for when you are simply too lazy to click, scroll, and read through endless websites yourself.

* **Hands-Free Web Browsing:** Watch Chromium navigate, click buttons, and read pages for you.
* **Open-Source Core:** Powered by the open-source [`browser-use`](https://github.com/browser-use/browser-use) library with zero vendor lock-in.
* **Grok 2 Vision Integration:** Lightning-fast visual grounding and snarky, concise summaries.
* **Dual Interface:** Run it in your terminal with rich ASCII art or launch the interactive Streamlit web dashboard.

---

## 🚀 Quickstart

### 1. Prerequisites & Virtual Environment
Ensure you have Python 3.11+ installed.

```bash
# Create and activate virtual environment
python -m venv .venv

# On Windows (PowerShell):
.\.venv\Scripts\Activate.ps1

# On macOS/Linux:
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. Configure API Key
Copy `.env.example` to `.env` and insert your [xAI API key](https://console.x.ai/):
```env
XAI_API_KEY=xai-your-api-key-here
GROK_MODEL=grok-2-vision-1212
HEADLESS=false
BROWSER_SLOW_MO=1000
```

---

## 🎮 Usage

### Option A: Interactive CLI Mode
```bash
python main.py
```
Presents you with a menu of 1-click preset missions or lets you type a custom lazy request.

### Option B: Streamlit Web Dashboard
```bash
streamlit run app.py
```
Launches an interactive web UI where you can adjust speed, model, toggle headless mode, and trigger sloth runs with a single click.

---

## 📁 Project Structure

```
├── .env                # API keys and browser settings
├── .env.example        # Template configuration
├── requirements.txt    # Python dependencies
├── main.py             # CLI runner
├── app.py              # Streamlit dashboard
├── test_agent.py       # Configuration verification script
├── DEVTO_SUBMISSION.md # Ready-to-publish Dev.to blog post
└── slothsurf/
    ├── __init__.py
    ├── config.py       # Environment loader
    ├── agent.py        # Core browser-use + Grok bridge
    ├── presets.py      # Pre-configured lazy missions
    └── ui.py           # Terminal styling and ASCII graphics
```

---

## 📜 Hackathon Theme & Open Source Narrative

See [`DEVTO_SUBMISSION.md`](DEVTO_SUBMISSION.md) for the complete hackathon writeup detailing why open-source agent harnesses outperform closed-source proprietary alternatives in privacy, developer freedom, and cost.
