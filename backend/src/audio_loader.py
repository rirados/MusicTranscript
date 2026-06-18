import librosa
import numpy as np

def load_audio(file_path: str, sr: int = 22050) -> tuple[np.ndarray, int]:
    """
    Load an audio file, converting it to mono and resampling.
    
    Design Decision: We enforce a standard sample rate (22050Hz) and mono channel
    to ensure consistent performance and behaviour for downstream DSP algorithms
    like spectral flux and pYIN.
    """
    # librosa.load naturally converts to mono and resamples if sr is provided
    y, sr = librosa.load(file_path, sr=sr, mono=True)
    return y, sr
