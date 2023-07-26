import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Caminho para o arquivo de áudio local
file_path = "cmajor.wav"

# Função para carregar o áudio a partir do arquivo
def load_audio(file_path):
    signal, sr = librosa.load(file_path, sr=None)
    return signal, sr

# Função para plotar o gráfico do sinal de áudio
def plot_waveform(signal, sr):
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(signal, sr=sr)
    plt.title("Sinal de Áudio")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Amplitude")
    plt.show()

# Função para calcular a Transformada de Fourier de um sinal
def compute_fft(signal):
    fft_result = np.fft.fft(signal)
    return fft_result

# Função para plotar o gráfico da Transformada de Fourier
def plot_fft(fft_result, sr):
    freqs = np.fft.fftfreq(len(fft_result), 1/sr)
    magnitude = np.abs(fft_result)
    plt.figure(figsize=(10, 4))
    plt.plot(freqs, magnitude)
    plt.title("Transformada de Fourier")
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Magnitude")
    plt.xlim(0, 500)
    plt.show()

# Função para plotar o espectrograma do sinal de áudio
def plot_spectrogram(signal, sr):
    D = librosa.amplitude_to_db(np.abs(librosa.stft(signal)), ref=np.max)
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(D, y_axis='linear', sr=sr, x_axis='time')
    plt.colorbar(format='%+2.0f dB')
    plt.xlabel('Tempo')
    plt.ylabel('Frequência')
    plt.title('Espectrograma')
    plt.tight_layout()
    plt.show()

# Carregar o áudio usando a função load_audio
signal, sr = load_audio(file_path)

# Plotar o sinal de áudio
plot_waveform(signal, sr)

# Calcular a Transformada de Fourier e plotar o gráfico
fft_result = compute_fft(signal)
plot_fft(fft_result, sr)

# Plotar o espectrograma do sinal de áudio
plot_spectrogram(signal, sr)
