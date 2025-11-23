import requests
import random

url = "http://localhost:8000/corridas"


data = {
    "id_corrida": random.randint(1000, 9999),
    "passageiro": {
        "nome": "Maria Silva", 
        "telefone": "99999-8888"
    },
    "motorista": {
        "nome": "Carlos",
        "nota": 4.9
    },
    "origem": "Centro",
    "destino": "Jardim",
    "forma_pagamento": "DigitalCoin",
    "valor": 42.50,
    "valor_corrida": 42.50
}

try:
    response = requests.post(url, json=data)
    print(" STATUS CODE:", response.status_code)
    print(" RESPOSTA COMPLETA:")
    print(response.json())
except Exception as e:
    print(" ERRO:", e)