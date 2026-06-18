# Build Basic UI and Server for Music Transcriber (React Version)

We will build out the API layer using FastAPI to expose the existing machine learning pipeline, and construct a premium-feeling React web application in a separate `frontend` folder.

## User Review Required

> [!IMPORTANT]
> Since we are using React, I will initialize the project using Vite (`npx -y create-vite@latest frontend --template react`) for a fast, modern setup. I will use standard CSS for styling to achieve the requested dark-mode, glassmorphic aesthetic without introducing extra UI libraries unless requested.

## Proposed Changes

### Backend Application Layer

#### [NEW] `d:\@PROJEX\music\backend\app.py`
We will create the FastAPI application here. It will:
1. Configure CORS to allow requests from the React frontend (running on a different port during development).
2. Provide a `POST /transcribe` endpoint that accepts an audio file upload.
3. Save the uploaded file temporarily, pass it to `src.pipeline.transcribe_audio`, clean up the temp file, and return the results.

### Frontend UI Layer (React)

#### [NEW] `d:\@PROJEX\music\frontend`
A new directory initialized via Vite.

#### [NEW] `d:\@PROJEX\music\frontend\src\App.jsx`
The main application component containing:
- A stylized drag-and-drop or file upload area.
- A loading state with micro-animations.
- A results section displaying the transcribed notes and a button to download the generated MIDI.

#### [NEW] `d:\@PROJEX\music\frontend\src\index.css`
Will contain the CSS custom properties (variables) for the design system, enforcing a vibrant, futuristic dark theme.



### Manual Verification
1. Start the backend: `cd backend && uvicorn app:app --reload`
2. Start the frontend: `cd frontend && npm install && npm run dev`
3. Open the frontend URL in the browser.
4. Upload `PianoRecordingsSingleNotes.wav` and verify the transcription flow works end-to-end.
