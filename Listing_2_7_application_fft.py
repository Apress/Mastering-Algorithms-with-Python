from Listing_2_6_fourier_transform_fft_ifft import fast_fourier_transform, inverse_fourier_transform
import numpy as np 
import matplotlib.pyplot as plt 

def generate_time_signal(sampling_rate = 256):
    sampling_interval = 1.0/sampling_rate
    t = np.arange(0,1,sampling_interval)

    frequency_1, frequency_2, frequency_3 = 5, 15, 25
    amplitude_1, amplitude_2, amplitude_3 = 20, 50, 100
    T1 = amplitude_1 * np.sin(2*np.pi*frequency_1*t)
    T2 = amplitude_2 * np.cos(2*np.pi*frequency_2*t)
    T3 = amplitude_3 * np.cos(2*np.pi*frequency_3*t)
    T = T1 + T2 + T3 
    return t, T, sampling_rate

def convert_signal_to_frequency_domain():
    t, T, sampling_rate = generate_time_signal()
    plt.figure(figsize = (12, 6))
    plt.subplot(121)
    plt.plot(t, T, 'b-', lw=2)
    plt.xlabel("Time / s", fontsize = 15)
    plt.ylabel('Amplitude', fontsize = 15)
    plt.title("Time spectrum", fontsize = 15)

    F=np.array(fast_fourier_transform(T))
    # calculate the frequency
    N = len(F)
    n = np.arange(N)
    frequency = n/(N/sampling_rate) 

    plt.subplot(122)
    markerline, stemlines, baseline = plt.stem(frequency, np.abs(F), 'b', markerfmt=" ", basefmt="-b")
    plt.setp(stemlines, 'linewidth', 2)
    plt.setp(baseline, 'linewidth', 2)
    plt.xlabel('Frequency (Hz)', fontsize = 15)
    plt.ylabel('FFT Amplitude |X(freq)|', fontsize = 15)
    plt.title("Frequency spectrum", fontsize = 15)
    plt.tight_layout()
    plt.show()

def low_high_pass_filter(cutoff_frequency, mode = "low_pass"): 
    t, T, sampling_rate = generate_time_signal()
    F=np.array(fast_fourier_transform(T))
    # calculate the frequency
    N = len(F)
    n = np.arange(N)
    frequency = n/(N/sampling_rate) 
    # set frequency at right half to 0
    F[N//2:] = 0

    # high pass and low pass 
    if mode == "low_pass":
        F[(frequency > cutoff_frequency)] = 0
    else:
        F[(frequency < cutoff_frequency)] = 0

    T = 2 * np.array(inverse_fourier_transform(F))

    plt.figure(figsize = (12, 6))
    plt.subplot(121)
    markerline, stemlines, baseline = plt.stem(frequency, np.abs(F), 'b', markerfmt=" ", basefmt="-b")
    plt.setp(stemlines, 'linewidth', 2)
    plt.setp(baseline, 'linewidth', 2)
    plt.xlim([0, frequency[N//2]])
    plt.xlabel('Frequency (Hz)', fontsize = 15)
    plt.ylabel('FFT Amplitude |X(freq)|', fontsize = 15)
    plt.title("Frequency spectrum, {} filter".format(' '.join(mode.split('_'))), fontsize = 15)

    plt.subplot(122)
    plt.plot(t, T, 'b-', lw=2, label = "Filtered waves")
    plt.xlabel("Time / s", fontsize = 15)
    plt.ylabel('Amplitude', fontsize = 15)
    plt.title("Time spectrum", fontsize = 15)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    convert_signal_to_frequency_domain()
    low_high_pass_filter(cutoff_frequency = 20, mode = "high_pass")
    low_high_pass_filter(cutoff_frequency = 6, mode = "low_pass")