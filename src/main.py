from fastapi import FastAPI
from src.producer import publish_corrida
from src.database.mongo_client import get_collection
from src.database.redis_client import redis_client
from src.models.corrida_model import CorridaInput
import uuid
from datetime import datetime

app = FastAPI()

@app.post("/corridas")
async def criar_corrida(corrida: CorridaInput):
    """
    Recebe uma corrida e publica a mensagem no RabbitMQ.
    """
    
    corrida_data = {
        "id_corrida": str(uuid.uuid4())[:8],
        "passageiro": {
            "nome": corrida.passageiro.nome,
            "telefone": corrida.passageiro.telefone
        },
        "motorista": {
            "nome": corrida.motorista.nome,
            "nota": corrida.motorista.nota
        },
        "origem": corrida.origem,
        "destino": corrida.destino,
        "valor_corrida": corrida.valor_corrida,
        "forma_pagamento": corrida.forma_pagamento,
        "valor": corrida.valor_corrida,
        "created_at": datetime.now().isoformat()
    }
    
    await publish_corrida(corrida_data)
    return {"status": "corrida enviada"}

@app.get("/corridas")
async def listar_corridas():
    """
    Lista até 100 corridas salvas no MongoDB.
    """
    coll = get_collection()
    docs = await coll.find().to_list(length=100)
    
    for doc in docs:
        doc.pop('_id', None)
    return docs

@app.get("/saldo/{motorista}")
async def consultar_saldo(motorista: str):
    """
    Consulta saldo do motorista no Redis
    """
    try:
        print(f"Consultando saldo para: {motorista}")
        
        
        if redis_client.client is None:
            print("Conectando ao Redis...")
            redis_client.connect()
        
        print(f"Redis client conectado: {redis_client.client is not None}")
        
        
        try:
            redis_client.client.ping()
            print("Redis ping bem-sucedido")
        except Exception as e:
            print(f"Redis ping falhou: {e}")
            return {"error": f"Redis não conectado: {str(e)}"}
        
        chave = f"saldo:{motorista.lower()}"
        print(f"Buscando chave: {chave}")
        
        saldo = redis_client.client.get(chave)
        print(f"Saldo retornado do Redis: {saldo}")
        
        if saldo is None:
            print("Saldo não encontrado, retornando 0")
            return {"motorista": motorista, "saldo": 0}
        
        print(f"Saldo encontrado: {saldo}")
        return {"motorista": motorista, "saldo": float(saldo)}
        
    except Exception as e:
        print(f"Erro geral: {e}")
        return {"error": f"Erro ao consultar saldo: {str(e)}"}

@app.get("/")
async def root():
    return {"message": "TransFlow API"}