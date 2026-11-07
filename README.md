# Music Transcriber

A web-based application that converts piano audio recordings into musical notes using audio signal processing.

## 1. Project Overview

Music Transcriber aims to help users identify the notes played in a piano recording.

The application accepts an audio file, analyzes the sound, identifies individual notes, and displays the detected musical information.

The initial version focuses on single-note piano melodies.

## 2. Project Objective

The main objectives are:

- Upload a piano recording in WAV format.
- Detect individual notes in the audio.
- Identify the pitch of each note.
- Convert detected frequencies into musical note names.
- Estimate the start time and duration of each note.
- Display the transcription through a web interface.
- Export the detected notes as a MIDI file.

## 3. How It Works

The application follows this general workflow:

1. **Audio Input:** The user uploads a piano recording.
2. **Audio Loading:** The audio file is loaded and converted into a format suitable for processing.
3. **Note Segmentation:** The audio is divided into individual note sections.
4. **Pitch Detection:** The frequency of each note is estimated.
5. **Note Mapping:** The detected frequency is converted into a musical note name, such as C3 or A4.
6. **Timing Analysis:** The start time and duration of each note are estimated.
7. **Output:** The detected notes are displayed and can be exported as a MIDI file.

## 4. Technologies Used

### Backend
- Python
- NumPy
- Librosa
- FastAPI

### Frontend
- React.js
- Vite
- CSS

### Audio Processing
- Digital Signal Processing (DSP)
- Pitch detection
- Frequency-to-note conversion
- Audio segmentation

## 5. Project Structure

```text
music-transcriber/
│
├── data/
│   └── all_notes.wav
│
├── notebooks/
│   └── exploration.ipynb
│
├── src/
│   ├── audio_loader.py
│   ├── segmentation.py
│   ├── pitch_detection.py
│   ├── note_mapper.py
│   ├── midi_export.py
│   └── pipeline.py
│
├── backend/
│   └── app.py
│
├── frontend/
│   ├── src/
│   └── ...
│
├── requirements.txt
└── README.md
```

### Folder and File Description

| File or Folder | Purpose |
|---|---|
| `data/` | Stores audio recordings used for testing. |
| `notebooks/` | Contains experiments and audio analysis. |
| `audio_loader.py` | Loads audio files. |
| `segmentation.py` | Identifies individual note sections. |
| `pitch_detection.py` | Detects the frequency of each note. |
| `note_mapper.py` | Converts frequencies into musical note names. |
| `midi_export.py` | Exports detected notes into MIDI format. |
| `pipeline.py` | Connects the audio processing steps. |
| `backend/app.py` | Provides the API using FastAPI. |
| `frontend/` | Contains the React web application. |
| `requirements.txt` | Lists Python dependencies. |

## 6. Setup and Installation

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd music-transcriber
```

### Step 2: Create a Python Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Start the Backend

Open a terminal in the project directory:

```bash
cd backend
uvicorn app:app --reload
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

### Step 5: Start the Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the local URL displayed by Vite in your browser.

## 7. Current Development Status

- [x] Audio loading and analysis
- [x] Initial pitch detection experiments
- [x] Frequency-to-note conversion
- [ ] Automatic note segmentation
- [ ] Complete transcription pipeline
- [ ] MIDI export
- [ ] FastAPI integration
- [ ] React frontend integration
- [ ] End-to-end testing

## 8. Future Enhancements

- Support for multiple instruments.
- Chord and polyphonic transcription.
- Sheet music generation.
- Tempo and rhythm estimation.
- Improved note detection accuracy.
- Music visualization through a piano keyboard.
- Support for additional audio formats.

## 9. Project Goal

The long-term goal is to develop a user-friendly music transcription application that converts audio recordings into readable musical information, helping musicians and music learners understand and reproduce melodies.
