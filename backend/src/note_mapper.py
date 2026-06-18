import librosa

def hz_to_note_info(hz: float) -> tuple[str, int]:
    """
    Map a frequency in Hz to its corresponding note name and MIDI number.
    
    Design Decision: Use librosa's built-in hz_to_note and hz_to_midi.
    We return both the human-readable note name (e.g., 'C4') and the MIDI number
    which is necessary for MIDI export.
    """
    # handle possible errors
    try:
        note_name = librosa.hz_to_note(hz)
        midi_number = round(librosa.hz_to_midi(hz))
        return note_name, midi_number
    except:
        return "Unknown", 0
