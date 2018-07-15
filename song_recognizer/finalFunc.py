from song_recognizer.Spectrogram import mic_audio
from song_recognizer.searchDatabase import search_database
from song_recognizer.song_to_fingerprint import song_to_fingerprint
from pathlib import Path
from os.path import join
from os import getcwd
import pickle

def identify(dur=10):
    '''
    Record an audio sample and match against the dictionary
    
    INPUTS
    
        dur:    length in seconds to record for
                integer
    
    OUTPUTS
    
        out:    name of matched song or -1 if song not found / dictionary not loaded
                string / integer
    '''
    if 'diction' not in globals():
        print("Dictionary not loaded. Call load() to load database.dat")
        return -1
    audio = mic_audio(dur)
    fings = song_to_fingerprint(audio)
    return search_database(diction, fings)

def accuracy(directory):
    '''
    TODO
    
    INPUTS
    
        directory:  location of folder containing cut samples (in subsequent folders with song names)
                    realtive to current working directory
                    string
    '''
    root = Path(directory)
    root.glob("*.mp3")
    print("NOT IMPLEMENTED")

def load(filename):
    '''
    Load the dictionary of encoded songs
    
    INPUTS:
    
        filename:   location of dictionary to load
                    realtive to current working directory
                    string
    '''
    globals()['diction'] = pickle.load(open(filename, 'rb'))
    print("Dictionary loaded")