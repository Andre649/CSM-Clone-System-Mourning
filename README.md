title: "Dataset de Vozes Emocionais com Marca d'Água"
description: "Projeto para criar e processar um dataset de vozes emocionais com marca d'água para cada emoção."

Dataset de Vozes Emocionais com Marca d'Água

Este projeto cria um dataset de vozes emocionais e aplica marcas d'água únicas a cada emoção para garantir autenticidade.

📌 Funcionalidades

✅ Baixa e processa áudios emocionais da base RAVDESS.

✅ Converte os áudios para um formato padronizado (44.1kHz).

✅ Aplica marcas d'água específicas para cada emoção.

✅ Verifica se um áudio possui uma marca d’água válida.

🚀 Como Usar

🔹 1️⃣ Baixar e Processar os Áudios

Execute o script de dataset para baixar e converter os áudios:

python dataset_emocoes.py

Isso criará uma pasta emotional_speech_dataset com os áudios processados e um metadata.csv.

🔹 2️⃣ Aplicar Marca d’Água

Para adicionar uma marca d’água a um áudio específico:

python watermarking.py --mode watermark --audio_path caminho/para/audio.wav --emotion happy

Altere happy para outra emoção desejada (neutral, sad, angry, etc.).

🔹 3️⃣ Verificar a Emoção de um Áudio

python watermarking.py --mode verify --audio_path caminho/para/audio.wav

Se o áudio tiver uma marca d’água válida, a emoção associada será exibida.

🎭 Emoções Suportadas

😊 Feliz (happy)

😡 Bravo (angry)

😢 Triste (sad)

😱 Surpreso (surprised)

😐 Neutro (neutral)

😨 Medo (fearful)

🤢 Nojo (disgust)

😌 Calmo (calm)

📂 Estrutura do Projeto

├── emotional_speech_dataset/
│   ├── raw/  # Áudios originais
│   ├── processed/  # Áudios convertidos
│   ├── watermarked/  # Áudios com marca d'água
│   ├── metadata.csv  # Emoções e caminhos dos áudios
├── dataset_emocoes.py  # Script de download e processamento
├── watermarking.py  # Script para marcação e verificação

📜 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

Desenvolvido para estudos de IA aplicada à geração de voz emocional. 🚀
