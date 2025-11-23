from pydantic import BaseModel

class Passageiro(BaseModel):
    nome: str
    telefone: str

class Motorista(BaseModel):
    nome: str
    nota: float

class CorridaInput(BaseModel):
    id_corrida: int
    passageiro: Passageiro
    motorista: Motorista
    origem: str
    destino: str
    forma_pagamento: str
    valor: float
    valor_corrida: float