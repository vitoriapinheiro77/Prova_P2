import requests
import time

base_url = "http://localhost:8000"

print(" TESTANDO SISTEMA COMPLETO...")


print("\n 1. Listando corridas...")
response = requests.get(f"{base_url}/corridas")
print("Status:", response.status_code)
print("Corridas:", response.json())


print("\n 2. Consultando saldo do Carlos...")
response = requests.get(f"{base_url}/saldo/carlos")
print("Status:", response.status_code)
print("Saldo:", response.json())


print("\n 3. Aguardando processamento assíncrono...")
time.sleep(3)


print("\n 4. Verificando após processamento...")
response = requests.get(f"{base_url}/corridas")
print("Corridas no MongoDB:", response.json())

response = requests.get(f"{base_url}/saldo/carlos") 
print("Saldo atualizado:", response.json())

print("\n Teste completo!")