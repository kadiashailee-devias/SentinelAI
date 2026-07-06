# 🌍 SentinelAI

AI-powered Disaster Response Multi-Agent System built with
Google ADK + Gemini + Streamlit.

---

## Problem

Disaster response requires rapid coordination between
multiple domains:

- Situation assessment
- Medical planning
- Supply logistics
- Information verification
- Report generation

Traditional systems are fragmented.

SentinelAI coordinates multiple AI agents into a single
decision-support platform.

---

## Features

✅ Google ADK Multi-Agent

✅ Incident Commander

✅ Google Search Tool

✅ Medical Agent

✅ Supply Agent

✅ Verification Agent

✅ Report Agent

✅ PDF Report Export

✅ Filesystem Storage

✅ Prompt Injection Detection

✅ Human Approval

---

## Architecture
![alt text](image.png)
---

## Folder Structure
sentinel_ai/

│

├── agents/

├── app/

├── tools/

├── security/

├── docs/

├── reports/

├── skills/

├── streamlit_app.py

├── requirements.txt

└── README.md


## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/sentinel_ai.git
cd sentinel_ai
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

```text
GOOGLE_API_KEY=YOUR_API_KEY
```



## Running the Project

Start the Streamlit application:

```bash
streamlit run streamlit_app.py
```

Open your browser:

```
http://localhost:8501
```

Enter an incident scenario, approve AI recommendations, and click **Launch Response**.


## Screenshots

### Dashboard

![Dashboard](docs/screenshots/Agent execution.png)

---

### Agent Execution

![Agents](docs/screenshots/output of execution.png)

---

### Incident Report

![Report](docs/screenshots/verification summary.png)


---

### Prompt Injection Detection

![Security](docs/screenshots/prompt injection output.png)



## Future Work

- Live disaster monitoring using official emergency APIs
- Real-time weather and satellite data integration
- Interactive disaster map visualization
- SMS and email alert notifications
- Resource optimization using AI planning
- Multi-language disaster assistance
- Voice-enabled emergency interaction
- Deployment on cloud infrastructure for large-scale use

## License

This project is licensed under the MIT License.

See the LICENSE file for details.