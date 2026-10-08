# SIGNEX Backend Architecture

## Sign → Speech
1. React captures a frame.
2. Frame is sent to FastAPI.
3. OpenCV decodes/processes the frame.
4. MediaPipe Hands extracts 21 landmarks.
5. Landmarks are normalized and converted to features.
6. Classifier predicts a sign.
7. Backend returns sign/text/confidence.
8. Browser or backend TTS produces speech.

## Speech/Text → Sign
1. Browser captures speech or text.
2. FastAPI receives the request.
3. STT converts speech to text when required.
4. Text is normalized.
5. Sign dictionary maps words/phrases to sign IDs.
6. Backend returns a sign sequence.
7. Godot maps IDs to 3D animations.

## Why REST + WebSocket
REST is suitable for discrete requests. WebSocket is suitable for a persistent real-time communication session where frames/results are continuously exchanged.
