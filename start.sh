#!/bin/bash

set -e

pip install transformers 
pip install huggingface_hub

# Exécutez le modèle
vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-14B &

# Attendez que le modèle soit prêt (ajustez le délai si nécessaire)
sleep 10

# Exécutez le script Python pour interagir avec le modèle
#python3 /app/main.py