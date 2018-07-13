import Spectrogram
import fingerprinting
from spectrogram_to_cutoff_and_peaks import *

def song_to_fingerprint(sample):
    S = Spectrogram.spectrogram(sample)
    cutoff = spectrogram_to_cutoff(S)
    peaks = spectrogram_to_peaks(S, cutoff)
    return fingerprinting.fingerprints(peaks)