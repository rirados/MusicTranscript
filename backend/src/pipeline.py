from dataclasses import dataclass
from typing import List, Optional
import io
import base64
from .audio_loader import load_audio
from .segmentation import detect_onsets
from .pitch_detection import estimate_pitch
from .note_mapper import hz_to_note_info
from .midi_export import create_midi

@dataclass
class NoteEvent:
    note_name: str
    frequency_hz: float
    midi_number: Optional[int]
    start_time: float
    end_time: float
    duration: float
    confidence: float = 1.0

def transcribe_audio(file_path: str) -> dict:
    """
    End-to-end pipeline to load audio, segment notes, estimate pitch, and generate results.
    
    Design Decision: Uses dataclasses to define the output contract (NoteEvent).
    Returns a dictionary suitable for JSON serialization in the FastAPI layer,
    including the base64-encoded MIDI file.
    """
    y, sr = load_audio(file_path)
    onsets = detect_onsets(y, sr)
    
    notes: List[NoteEvent] = []
    
    # Append the end of the audio as the final boundary
    boundaries = list(onsets) + [len(y) / sr]
    
    for i in range(len(boundaries) - 1):
        start_time = boundaries[i]
        end_time = boundaries[i+1]
        duration = end_time - start_time
        
        # Skip very short notes
        if duration < 0.05:
            continue
            
        freq = estimate_pitch(y, sr, start_time, end_time)
        
        if freq is not None:
            note_name, midi_num = hz_to_note_info(freq)
            note_event = NoteEvent(
                note_name=note_name,
                frequency_hz=round(freq, 2),
                midi_number=midi_num,
                start_time=round(start_time, 3),
                end_time=round(end_time, 3),
                duration=round(duration, 3)
            )
            notes.append(note_event)
            
    # Generate MIDI
    midi_obj = create_midi(notes)
    mem_file = io.BytesIO()
    midi_obj.writeFile(mem_file)
    midi_b64 = base64.b64encode(mem_file.getvalue()).decode('ascii')
    
    return {
        "notes": [note.__dict__ for note in notes],
        "midi_base64": midi_b64
    }
