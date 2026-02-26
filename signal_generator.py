import time

def get_sin_wave_amplitude(freq, time):
    from math import sin, pi
    raw = sin(2.0 * pi * freq * time) + 1
    
    return raw / 2.0

def wait_for_sampling_period(sampling_frequency):
    period = 1.0 / sampling_frequency
    time.sleep(period)

def get_triangle_wave_amplitude(freq, time):
    period = 1.0 / freq
    time %= period
    if time < period / 2:
        return time / (period / 2)
    else:
        time %= period / 2
        return 1 - time / (period / 2)