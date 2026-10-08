def normalize_landmarks(landmarks):
    if not landmarks: return []
    wrist=landmarks[0]
    return [(p.x-wrist.x,p.y-wrist.y,p.z-wrist.z) for p in landmarks]
