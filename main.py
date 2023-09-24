import io
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from bark import (
    create_audio_buffer,
    run_inference,
)
from fastapi.responses import StreamingResponse

app = FastAPI()

# Add CORS middleware
origins = [
    "http://localhost",
    "http://localhost:3000",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/bark-inference", response_class=Response)
async def run_bark_inference_endpoint(request: Request):
    data = await request.json()
    text = data.get("text", "")
    voice = data.get("voice", None)
    audio_array = run_inference(text, voice)
    audio_buffer = create_audio_buffer(audio_array)
    return StreamingResponse(io.BytesIO(audio_buffer), media_type="audio/wav")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
