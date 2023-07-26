# # Análise de Áudio com Librosa

Este é um projeto de análise de áudio utilizando a biblioteca Librosa para carregar e processar o sinal de áudio. O objetivo é realizar a plotagem do sinal de áudio, calcular a Transformada de Fourier e o espectrograma.

## Como Executar

Para executar o projeto, siga os passos abaixo:

1. Clone o repositório para o seu ambiente local.

2. Instale as dependências necessárias utilizando o comando:

3. Defina o caminho para o arquivo de áudio na variável `file_path` no arquivo `main.py`.

4. Execute o script `main.py` para carregar e analisar o áudio.

## Funções Implementadas

- `load_audio(file_path)`: Função para carregar o áudio a partir do arquivo utilizando a biblioteca Librosa.

- `plot_waveform(signal, sr)`: Função para plotar o gráfico do sinal de áudio (forma de onda) em função do tempo.

- `compute_fft(signal)`: Função para calcular a Transformada de Fourier do sinal de áudio.

- `plot_fft(fft_result, sr)`: Função para plotar o gráfico da Transformada de Fourier (magnitude em função da frequência).

- `plot_spectrogram(signal, sr)`: Função para calcular e plotar o espectrograma do sinal de áudio, com as amplitudes em escala de decibéis.

## Resultados

O projeto irá carregar o sinal de áudio, plotar o gráfico do sinal de áudio, calcular a Transformada de Fourier e plotar o gráfico da Transformada de Fourier. Em seguida, calculará e plotará o espectrograma do sinal de áudio.
# Sinal de Áudio
<p align="center"><img src="./img/1.png" width="500"></p>

# Fourier 
<p align="center"><img src="./img/2.png" width="500"></p>

# Espectrograma
<p align="center"><img src="./img/3.png" width="500"></p>
<p align="center"><img src="./img/4.png" width="500"></p>

## Observações

- Certifique-se de ter os pacotes necessários instalados antes de executar o projeto.
- O caminho para o arquivo de áudio deve ser definido corretamente na variável `file_path`.
- Os resultados serão exibidos em gráficos na saída do console.
