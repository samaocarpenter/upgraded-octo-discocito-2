from song_recognizer.song_to_fingerprint import *
from song_recognizer.Spectrogram import mic_audio
from pickle import load
import song_recognizer.searchDatabase as search

def getTheSong(time = 5):
    sample = mic_audio(time)
    fingy = song_to_fingerprint(sample)
    database = load(open('database.dat', 'rb'))
    print(search.search_database(database, fingy))
