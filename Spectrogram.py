
# coding: utf-8

# In[3]:


import microphone
import numpy as np
get_ipython().run_line_magic('matplotlib', 'notebook')
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from microphone import record_audio
from IPython.display import Audio
from scipy import signal


# In[21]:


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

    #print(audio_file)
    S, freqs, times = mlab.specgram(audio_file, NFFT=4096, Fs=sampling_rate,window=mlab.window_hanning,noverlap=2048)
    
    #print(S.shape)
    return S


# In[23]:


def mic_audio(dur):
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


# In[24]:


#mic_audio(5)

