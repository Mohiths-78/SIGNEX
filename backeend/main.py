from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from .routers import health, sign, speech, avatar

app = FastAPI(title='SIGNEX API', description='Bidirectional sign-language communication backend', version='1.0.0')
app.add_middleware(CORSMiddleware, allow_origins=['http://localhost:5173'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
app.include_router(health.router, prefix='/api')
app.include_router(sign.router, prefix='/api')
app.include_router(speech.router, prefix='/api')
app.include_router(avatar.router, prefix='/api')

@app.websocket('/ws/live')
async def live(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({'type':'status','message':'SIGNEX live channel connected'})
    try:
        while True:
            data = await websocket.receive_json()
            await websocket.send_json({'type':'echo','received':data})
    except Exception:
        pass
