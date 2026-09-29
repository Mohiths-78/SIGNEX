# SIGNEX — Bidirectional Sign Language Communication Platform

SIGNEX is a web-based accessibility platform for real-time communication between Deaf individuals and hearing users. It combines **React + FastAPI + Python + OpenCV + MediaPipe + speech processing + a planned Godot 3D avatar**.

## Core communication flows

### 1. Sign → Text → Speech
```text
Browser Camera → FastAPI → OpenCV → MediaPipe Hands → 21 Landmarks → Gesture Classifier → Text → TTS
```

### 2. Speech/Text → Sign
```text
Browser Microphone/Text → FastAPI → Speech-to-Text → Text → Sign Dictionary → Sign IDs → Godot 3D Avatar
```

### 3. Continuous mode
```text
React Browser ↔ WebSocket ↔ FastAPI ↔ Recognition/Speech/Sign Services
```

## Architecture
```text
SIGNEX WEBSITE (React/Vite)
        │
        ├── Camera
        ├── Microphone
        └── Text input
        │
   REST API / WebSocket
        │
PYTHON BACKEND (FastAPI)
        │
 ┌──────┼───────────┐
 │      │           │
OpenCV MediaPipe  Speech-to-Text
 │      │           │
 └── Gesture/Text Engine ──┐
                            │
              ┌─────────────┴────────────┐
              ▼                          ▼
        Text + TTS                 Sign Mapping
                                         │
                                         ▼
                                  Godot 3D Avatar
```

## Repository structure
```text
SIGNEX/
├── frontend/                 # React/Vite website
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routers/           # API endpoints
│   │   └── services/          # CV, speech, mapping services
│   ├── data/gestures.json
│   └── requirements.txt
├── avatar/                   # Godot integration
├── docs/                     # Architecture documentation
├── .gitignore
└── README.md
```

## API
| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/health` | Backend health check |
| POST | `/api/sign/recognize` | Image/sign recognition |
| POST | `/api/speech/transcribe` | Speech-to-text |
| POST | `/api/text/to-sign` | Text to sign sequence |
| WS | `/ws/live` | Continuous communication |

FastAPI Swagger UI: `http://localhost:8000/docs`

## Setup

### Backend
```bash
cd backend
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Backend: `http://localhost:8000`

### Frontend
```bash
cd frontend
npm install
npm run dev
```
Frontend normally runs at `http://localhost:5173`.

## Recognition pipeline
The intended first implementation is:
```text
Webcam → OpenCV → MediaPipe Hands → 21 landmarks → normalization → ML/rule classifier → sign → text → speech
```
The current backend deliberately leaves the trained model as an integration point. This lets the team add its own ISL dataset/model without changing the API structure.

## Text-to-sign pipeline
```text
Text → normalization → gesture dictionary → sign IDs → Godot animation
```
Example:
```json
{"text":"hello one","signs":["HELLO","ONE"]}
```

## Technology stack
- Frontend: React, Vite, JavaScript, Camera/Microphone Web APIs
- Backend: Python, FastAPI, Uvicorn
- Computer vision: OpenCV, MediaPipe, NumPy
- ML: Scikit-learn or a later deep-learning model
- Speech: Vosk / SpeechRecognition / another selected STT engine
- TTS: pyttsx3 or browser SpeechSynthesis
- Avatar: Godot 3D
- Storage: JSON initially; SQLite/PostgreSQL later

## Development roadmap
1. Connect webcam frames to `/api/sign/recognize`.
2. Add MediaPipe 21-landmark extraction.
3. Normalize landmarks relative to the wrist.
4. Train/load the ISL gesture classifier.
5. Add confidence and prediction smoothing.
6. Add speech recognition.
7. Expand `gestures.json` into an ISL vocabulary/database.
8. Add dynamic/continuous sign recognition.
9. Connect Godot animations to sign IDs.
10. Replace REST polling with WebSocket streaming for live communication.
11. Add sector-specific vocabulary for Hospitality, Financial Services, Entertainment and Retail.

## Important scope note
The first version should be described as **real-time gesture/sign recognition**, not complete natural-language ISL translation. Full continuous sign-language translation can require temporal movement, two-hand/body information, facial/non-manual features, sign transitions and language context.

## GitHub publishing
```bash
git init
git add .
git commit -m "Initial SIGNEX web and backend architecture"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/SIGNEX.git
git push -u origin main
```

Before publishing, replace `YOUR_USERNAME`, add your actual trained model/dataset documentation, and update the license/credits for any third-party code or datasets.
