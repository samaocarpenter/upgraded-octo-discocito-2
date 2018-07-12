from pathlib import Path
from librosa import load
import numpy as np
import microphone
import matplotlib.mlab as mlab

def songCollector(path = '.'):
    '''
    A generator object that yields each song presently in the folder.
    
    OPTIONAL INPUT:
        path: The computer path in which the songs are located. By default,
        it assumes that they are located in the same folder as the program.
        
    OUTPUTS:
        file: The name of the file.
        f: The song data itself.
    '''
    
    root = Path(path)
    files = root.glob('*.mp3')
    for file in files:
        data, fsdfs = load(file, sr = 44100, mono = True)
        yield file, data
        

def create_spectrogram(audio_file, sampling_rate = 44100):
    """ Given bytes from an audio recording, returns the spectrogram
    
        Parameters
        ----------
        audio_file: numpy.ndarray, length N
        
        sampling_rate: int, rate at which audio was sampled
        
        
        Returns
        -------
        S: numpy.ndarray, shape = (N,M)
            int spectrogram array"""

    #audio_file = np.hstack([np.frombuffer(i,np.int16) for i in audio_file])
    #print(audio_file)
    S, freqs, times = mlab.specgram(audio_file, NFFT=4096, Fs=sampling_rate,window=mlab.window_hanning,noverlap=2048)
    
    #print(S.shape)
    return S

def mic_audio(dur = 10):
    """ Given duration for audio recording, records for that time and converts to digital audio signal.
    
        Parameters
        ----------
        dur: int, duration for recording
        
        
        Returns
        -------
        S: numpy.ndarray, shape = (N,M)
            int spectrogram array"""

    audio,b = microphone.record_audio(dur)
    audio = np.hstack([np.frombuffer(i,np.int16) for i in audio])
    return audio
