import librosa
import numpy as np

def detect_onsets(y: np.ndarray, sr: int) -> np.ndarray:
    """
    Detect note boundaries using spectral flux onset detection.
    
    Design Decision / Algorithm Explanation:
    Spectral flux measures how quickly the power spectrum of a signal changes.
    We compute a spectrogram, then look at the positive differences in magnitude 
    between successive frames. Large positive changes indicate an onset (the start of a note).
    Using `librosa.onset.onset_detect` abstracts this by picking peaks in the onset envelope.
    """
    # Detect onset frames
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr, wait=1, pre_max=1, post_max=1, pre_avg=3, post_avg=3, delta=0.05, wait=3)
    # Convert frames to time (seconds)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)
    return onset_times
