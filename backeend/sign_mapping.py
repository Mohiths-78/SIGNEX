import json
from pathlib import Path
DATA=Path(__file__).resolve().parents[2]/'data'/'gestures.json'
def text_to_signs(text):
    with open(DATA,encoding='utf-8') as f: data=json.load(f)
    words=text.strip().lower().split()
    return {'text':text,'signs':[data.get(w,{'sign_id':'UNKNOWN'})['sign_id'] for w in words]}
