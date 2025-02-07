import numpy as np
from scipy.io.wavfile import write

def save_wav(data, filename, sample_rate):
    """保存音频为WAV文件"""
    scaled = np.int16(data * 32767)
    write(filename, sample_rate, scaled)
