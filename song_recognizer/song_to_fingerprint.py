from song_recognizer.Spectrogram import create_spectrogram
from song_recognizer.fingerprinting import fingerprints
from song_recognizer.spectrogram_to_cutoff_and_peaks import spectrogram_to_cutoff, spectrogram_to_peaks

def song_to_fingerprint(sample):
    print("Creating spectrogram... ", end='')
    S = create_spectrogram(sample)
    print("done")
    print("Finding cutoff... ", end='')
    cutoff = spectrogram_to_cutoff(S)
    print("done")
    print("Finding peaks... ", end='')
    peaks = spectrogram_to_peaks(S, cutoff)
    print("done")
    print("Fingerprinting... ", end='')
    fings = fingerprints(peaks)
    print("done")
    return fings