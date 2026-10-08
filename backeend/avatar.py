from fastapi import APIRouter
from pydantic import BaseModel
from ..services.sign_mapping import text_to_signs
router=APIRouter(tags=['Avatar'])
class TextRequest(BaseModel): text:str
@router.post('/text/to-sign')
def text_to_sign(req:TextRequest): return text_to_signs(req.text)
