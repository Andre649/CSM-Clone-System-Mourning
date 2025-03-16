import argparse
import os
import silentcipher
import torch
import torchaudio
import pandas as pd

# Chaves de marca d'água para cada emoção
EMOTION_WATERMARKS = {
    "neutral": [101, 102, 103, 104, 105],
    "calm": [201, 202, 203, 204, 205],
    "happy": [301, 302, 303, 304, 305],
    "sad": [401, 402, 403, 404, 405],
    "angry": [501, 502, 503, 504, 505],
    "fearful": [601, 602, 603, 604, 605],
    "disgust": [701, 702, 703, 704, 705],
    "surprised": [801, 802, 803, 804, 805],
}

def load_watermarker(device: str = "cuda") -> silentcipher.server.Model:
    model = silentcipher.get_model(
        model_type="44.1k",
        device=device,
    )
    return model

@torch.inference_mode()
def watermark(audio_path: str, emotion: str):
    if emotion not in EMOTION_WATERMARKS:
        raise ValueError(f"Emoção '{emotion}' não reconhecida.")
    
    watermarker = load_watermarker(device="cuda")
    watermark_key = EMOTION_WATERMARKS[emotion]
    
    audio_array, sample_rate = torchaudio.load(audio_path)
    audio_array_44khz = torchaudio.functional.resample(audio_array, orig_freq=sample_rate, new_freq=44100)
    encoded, _ = watermarker.encode_wav(audio_array_44khz, 44100, watermark_key, calc_sdr=False, message_sdr=36)
    
    torchaudio.save(audio_path.replace("processed", "watermarked"), encoded, 44100)
    print(f"Áudio {audio_path} foi marcado com a emoção {emotion}!")

@torch.inference_mode()
def verify(audio_path: str) -> str:
    watermarker = load_watermarker(device="cuda")
    audio_array, sample_rate = torchaudio.load(audio_path)
    audio_array_44khz = torchaudio.functional.resample(audio_array, orig_freq=sample_rate, new_freq=44100)
    result = watermarker.decode_wav(audio_array_44khz, 44100, phase_shift_decoding=True)
    
    if result["status"]:
        for emotion, key in EMOTION_WATERMARKS.items():
            if result["messages"][0] == key:
                return f"Áudio pertence à emoção: {emotion}"
    return "Áudio não tem marca d'água reconhecida."

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str, required=True, choices=["watermark", "verify"], help="Modo de operação: watermark ou verify")
    parser.add_argument("--audio_path", type=str, required=True, help="Caminho do arquivo de áudio")
    parser.add_argument("--emotion", type=str, help="Emoção associada (necessária para watermark)")
    args = parser.parse_args()
    
    if args.mode == "watermark":
        if not args.emotion:
            raise ValueError("A emoção deve ser especificada para marcação de áudio.")
        watermark(args.audio_path, args.emotion)
    elif args.mode == "verify":
        resultado = verify(args.audio_path)
        print(resultado)