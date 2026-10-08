import cv2, numpy as np

def recognize_image(image_bytes: bytes):
    frame=cv2.imdecode(np.frombuffer(image_bytes,np.uint8),cv2.IMREAD_COLOR)
    if frame is None: return {'sign':'UNKNOWN','text':'Invalid image','confidence':0.0}
    # TODO: BGR->RGB -> MediaPipe Hands -> 21 landmarks -> normalize -> classifier.
    return {'sign':'UNKNOWN','text':'Recognition pipeline ready for MediaPipe/model integration','confidence':0.0}
