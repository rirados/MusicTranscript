import librosa
import numpy as np

def estimate_pitch(y: np.ndarray, sr: int, start_time: float, end_time: float) -> float | None:
    """
    Estimate the pitch (in Hz) of a segment using pYIN.
    
    Design Decision / Algorithm Explanation:
    The probabilistic YIN (pYIN) algorithm is designed for monophonic pitch estimation.
    It extends the classic YIN algorithm (which relies on autocorrelation) by adding 
    probabilistic distributions over multiple pitch candidates. 
    It then uses a Hidden Markov Model (HMM) to decode the most likely sequence of pitches,
    effectively smoothing the results and eliminating octave errors or spurious jumps.
    """
    start_sample = int(start_time * sr)
    end_sample = int(end_time * sr)
    segment = y[start_sample:end_sample]
    
    if len(segment) == 0:
        return None
        
    try:
        f0, voiced_flag, voiced_prob = librosa.pyin(
            segment, 
            fmin=librosa.note_to_hz('C2'), 
            fmax=librosa.note_to_hz('C7'), 
            sr=sr,
            frame_length=2048,
            hop_length=512
        )
        
        voiced_f0 = f0[voiced_flag]
        if len(voiced_f0) > 0:
            return float(np.median(voiced_f0))
    except Exception as e:
        pass
    return None
