import numpy as np
import time

def get_sin_wave_amplitude (freq, time):
    return 0.5*np.sin(2*np.pi*freq*time) + 1

