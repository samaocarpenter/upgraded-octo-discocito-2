import numpy as np

from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion 
from scipy.ndimage.morphology import iterate_structure

def spectrogram_to_cutoff(spectrogram, frac_cut = 0.9):
    """ Given the values of a spectrogram, return the cutoff value that 
        distinguishes the foreground from the background.
        
        Parameters
        ----------
        spectrogram : numpy.ndarray, shape = (N, M)
            2D array of shape (N, M)
            
        frac_cut : int
            the percentage of lower amplitudes that will be considered 
            background
            
        Returns
        -------
        The cutoff value used to distinguish the foreground from the 
        background. """
        
    #spectrogram[spectrogram <= 0] = 1e-15
    spectrogram += 1e-20
    
    flat_spec = np.log(spectrogram.flatten())
    N = len(flat_spec)
    
    bin_counts, bin_edges = np.histogram(flat_spec, bins = int(N / 2), density = True)
    bin_size = np.diff(bin_edges)
    
    cumulative_distr = np.cumsum(bin_counts * bin_size)
    
    bin_index_of_cutoff = np.searchsorted(cumulative_distr, frac_cut)
    
    # given the bin-index, we want the associated log-amplitude value for that bin
    cutoff = bin_edges[bin_index_of_cutoff]
    return cutoff

def spectrogram_to_peaks(spectrogram, cutoff, iterations = 3):
    """ Given a spectrogram, return its peaks, which are all local peaks
        with values greater than the cutoff. 
        
        Parameters
        ----------
        spectrogram : numpy.ndarray, shape = (N, M)
            2D array of shape (N, M)
            
        cutoff : float
            elements less than or equal to the cutoff are considered 
            background elements
            
        iterations : int
            the number of iterations for the iterated footprint
            
        Returns
        -------
        A bool array of the peaks of a spectrogram. """
    
    fp = generate_binary_structure(rank = 2, connectivity = 1)
    spec_max = maximum_filter(spectrogram, footprint = iterate_structure(fp, iterations))
    return (spectrogram == spec_max) & (spectrogram > cutoff)