import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import IPython.display as ipd
from synthesis import create_audio_wave

def calculate_melsp(x, n_fft=1024, hop_length=128, n_mels=128):
    stft = np.abs(librosa.stft(x, n_fft=n_fft, hop_length=hop_length))**2
    log_stft = librosa.power_to_db(stft)
    melsp = librosa.feature.melspectrogram(S=log_stft, n_mels=n_mels)
    return melsp

# display wave in plots
def show_wave(x):
    plt.plot(x)
    plt.show()
    
    
# display wave in heatmap
def show_melsp(melsp, fs):
    librosa.display.specshow(melsp, sr=fs)
    plt.colorbar()
    plt.show()


if __name__ == '__main__':
    max_len = 500
    fs = 25000
    text1 = "I never made it to sixth grade, kid."
    text2 = "it dose not look like you are gonna"
    wav = create_audio_wave(text1, max_len, transformaer_pth_step = 160000, postnet_pth_step=100000, save = None)

    print(wav.shape)  # (137225,)
    show_wave(wav)

    melsp = calculate_melsp(wav, n_fft=fs, hop_length=max_len, n_mels=max_len)
    print(melsp.shape) # (500, 275)

    show_melsp(melsp, fs)

    # 実際にjupyter上で音声が聞ける
    ipd.Audio(wav, rate=fs)