# -*- coding: utf-8 -*-
"""Natty or Not - IA Generativa no Fisiculturismo

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J-euYn3ZFWULuCTiGAM1Pg-U028sZaTi
"""

!pip install gtts

!pip install transformers torch pillow gtts


import torch
import requests
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
from io import BytesIO
from gtts import gTTS
import IPython.display as ipd, IPython.display as display

model_name = "EleutherAI/gpt-neo-1.3B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def gerar_texto_natty():
    prompt = (
        "Escreva um texto detalhado sobre os desafios de se manter natural (natty) no fisiculturismo. "
        "Explique os benefícios, dificuldades e diferenças em relação ao uso de substâncias sintéticas. "
        "Seja informativo e estruturado."
    )

    inputs = tokenizer(prompt, return_tensors="pt")

    output = model.generate(
        **inputs,
        max_length=300,
        pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=3,
        do_sample=True,
        temperature=0.6,
        top_k=30,
        top_p=0.85
    )

    return tokenizer.decode(output[0], skip_special_tokens=True)


def texto_para_audio(texto):
    tts = gTTS(text=texto, lang="pt")
    tts.save("natty_or_not.mp3")
    return "natty_or_not.mp3"


def exibir_imagem_natty():
    image_url = "https://images.pexels.com/photos/1552252/pexels-photo-1552252.jpeg"

    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content)).convert("RGB")
        display.display(image)
    else:
        print("❌ Erro ao carregar a imagem. Verifique o URL.")


texto_gerado = gerar_texto_natty()
print("📜 Texto Gerado:\n")
print(texto_gerado)


arquivo_audio = texto_para_audio(texto_gerado)
ipd.display(ipd.Audio(arquivo_audio))

exibir_imagem_natty()

print("\n🚀 Código executado com sucesso! Texto gerado, áudio criado e imagem exibida.")