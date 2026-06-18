from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import os
import shutil

from src.pipeline import transcribe_audio

app = FastAPI(title="Music Transcriber API")

# Allow requests from the React development server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    if not file.filename.endswith(".wav"):
        raise HTTPException(status_code=400, detail="Only .wav files are supported.")
    
    # Save the uploaded file to a temporary location
    try:
        # Create a temporary file that is automatically deleted when closed
        # But we need its path for librosa, so we manage deletion manually
        fd, temp_path = tempfile.mkstemp(suffix=".wav")
        os.close(fd)
        
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # Run the transcription pipeline
        results = transcribe_audio(temp_path)
        
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Clean up the temp file
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.1", port=8000)
