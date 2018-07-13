import numpy as np

def fingerprints(specgram, fanout=5):
    '''
    Analyzes a peaks spectrogram and extracts pairwise fingerprints

    INPUTS

        specgram:   spectrogram to analyze
                    boolean ndarray of shape (num_freqs, num_times)
                    same shape as first output from mlab.spec()

        fanout:     number of neighboring points each point gets matched against
                    integer

    OUTPUTS
    
        out:        list of pairs of featues with corresponding times
                    ndarray of shape (?, 2) containing (f_n+1, f_n, f_n+1-t_n) and t_n
    '''
    
    # sorted by dim 0 (time)
    t, f = np.where(specgram.T)

    # choose pairs to encode
    out = np.empty((1, 2))
    for i in range(len(t)):
        for j in range(i+1, min(i+1+fanout, len(t))):
            out = np.append(out, [[(f[i], f[j], t[j]-t[i]), t[i]]], axis=0)
    return out[1:, :]

def add_to_dict(diction, fings, song_id):
    '''
    Add results of fingerprints() to an existing (or empty) dictionary

    INPUTS

        diction:    dictionary to modify
        
        fings:      output from fingerprints()

        song_id:    id to catalogue the song as

    OUTPUTS

        out:        same dictionary as diction
    '''
    for fing in fings:
        tup = (song_id, fing[1])
        if(fing[0] in diction):
            diction[fing[0]].append(tup)
        else:
            diction[fing[0]] = [tup]
    return diction
