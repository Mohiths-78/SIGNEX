from fastapi import APIRouter, File, UploadFile
from ..services.gesture_recognition import recognize_image
router=APIRouter(prefix='/sign',tags=['Sign'])
@router.post('/recognize')
async def recognize(file: UploadFile=File(...)):
    return recognize_image(await file.read())
