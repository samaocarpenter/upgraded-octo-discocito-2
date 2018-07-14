import song_recognizer.Spectrogram as Spectrogram
import song_recognizer.fingerprinting as fingerprinting
from song_recognizer.spectrogram_to_cutoff_and_peaks import spectrogram_to_cutoff, spectrogram_to_peaks

def song_to_fingerprint(sample):
    S = Spectrogram.create_spectrogram(sample)
    cutoff = spectrogram_to_cutoff(S)
    peaks = spectrogram_to_peaks(S, cutoff)
    return fingerprinting.fingerprints(peaks)
