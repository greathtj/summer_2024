import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram
import pandas as pd

# Constants
CSV_FILENAME = 'vibration_data.csv'
OUTPUT_IMAGE_FILENAME = 'spectrogram.jpg'

def read_accx_from_csv(filename):
    data = pd.read_csv(filename)
    accx = data['AccX'].values.astype(float)
    return accx

def plot_and_save_spectrogram(data, fs, output_filename):
    f, t, Sxx = spectrogram(data, fs)
    plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [s]')
    plt.title('Spectrogram of AccX')
    plt.colorbar(label='Intensity [dB]')
    plt.savefig(output_filename)
    plt.close()

if __name__ == '__main__':
    accx_data = read_accx_from_csv(CSV_FILENAME)
    sampling_rate = 500  # Hz, adjust according to your data
    plot_and_save_spectrogram(accx_data, sampling_rate, OUTPUT_IMAGE_FILENAME)
    print(f"Spectrogram saved as {OUTPUT_IMAGE_FILENAME}")
