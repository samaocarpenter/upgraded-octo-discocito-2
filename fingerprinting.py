import numpy as np

def fingerprints(specgram, fanout=5):
    '''
    INPUTS

        specgram:   spectrogram to analyze
                    boolean ndarray of shape (num_feqs, num_times)
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
