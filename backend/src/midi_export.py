from midiutil import MIDIFile
from typing import List, Any

def create_midi(notes: List[Any], tempo: int = 120) -> MIDIFile:
    """
    Generate a MIDIFile object from a sequence of NoteEvent objects.
    
    Design Decision: We use MIDIUtil for its simplicity in writing programmatic MIDI.
    Assuming a default tempo (120 BPM). Time and duration need to be converted to beats.
    At 120 BPM, 1 beat = 0.5 seconds. 
    """
    midi = MIDIFile(1)  # One track
    track = 0
    time_offset = 0
    midi.addTrackName(track, time_offset, "Transcribed Piano")
    midi.addTempo(track, time_offset, tempo)
    
    bps = tempo / 60.0
    
    for note in notes:
        if note.midi_number is not None and note.midi_number > 0:
            start_beat = note.start_time * bps
            duration_beat = note.duration * bps
            
            # Channel 0, volume 100
            midi.addNote(track, channel=0, pitch=note.midi_number, time=start_beat, duration=duration_beat, volume=100)
            
    return midi
