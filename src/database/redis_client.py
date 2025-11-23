import redis
import os

class RedisClient:
    def __init__(self):
        self.client = None
        
    def connect(self):
        try:
            self.client = redis.Redis.from_url(
                os.getenv("REDIS_URL"),
                decode_responses=True
            )
            self.client.ping()
            print(" Conectado ao Redis")
        except Exception as e:
            print(f" Erro ao conectar Redis: {e}")


redis_client = RedisClient()


def salvar_corrida(id_corrida: str, dados: dict):
    """Salva uma corrida no Redis como um hash."""
    if redis_client.client is None:
        redis_client.connect()
    redis_client.client.hset(f"corrida:{id_corrida}", mapping=dados)

def obter_corrida(id_corrida: str):
    """Retorna os dados de uma corrida salva no Redis."""
    if redis_client.client is None:
        redis_client.connect()
    return redis_client.client.hgetall(f"corrida:{id_corrida}")

def listar_corridas():
    """Lista todas as corridas salvas no Redis."""
    if redis_client.client is None:
        redis_client.connect()
    keys = redis_client.client.keys("corrida:*")
    return {key: redis_client.client.hgetall(key) for key in keys}