import motor.motor_asyncio
from faststream import FastStream
from faststream.rabbit import RabbitBroker
from dotenv import load_dotenv
import redis
import os
import json


load_dotenv()


RABBIT_URL = os.getenv("RABBITMQ_URL")
MONGO_URL = os.getenv("MONGODB_URL")
REDIS_URL = os.getenv("REDIS_URL")

print("RabbitMQ URL:", RABBIT_URL)
print("Mongo URL:", MONGO_URL)
print("Redis URL:", REDIS_URL)


broker = RabbitBroker(RABBIT_URL)
app = FastStream(broker)


mongo_client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = mongo_client["transflow"]
coll = db["corridas"]


redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)


@broker.subscriber("corrida_finalizada") 
async def receber_corrida(msg: dict):
    try:
        print("Mensagem recebida:", msg)
        
        
        await coll.insert_one(msg)
        print("Corrida salva no MongoDB!")
        
        
        motorista_nome = msg["motorista"]["nome"].lower()
        valor_corrida = msg["valor_corrida"]
        
        redis_client.incrbyfloat(f"saldo:{motorista_nome}", valor_corrida)
        novo_saldo = redis_client.get(f"saldo:{motorista_nome}")
        
        print(f"Saldo atualizado - {motorista_nome}: R$ {novo_saldo}")
        
    except Exception as e:
        print(f"Erro ao processar corrida: {e}")


if __name__ == "__main__":
    import asyncio
    asyncio.run(app.run())