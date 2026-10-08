from fastapi import APIRouter, File, UploadFile
from ..services.speech_service import transcribe_audio
router=APIRouter(prefix='/speech',tags=['Speech'])
@router.post('/transcribe')
async def transcribe(file: UploadFile=File(...)): return transcribe_audio(await file.read())
