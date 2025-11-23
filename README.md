# Prova_P2

# Passos de Instalação

Pré-requisitos

- Docker instalado

- Docker Compose instalado

- Git para clonar o repositório

# Instalação Passo a Passo

- Clone o repositório

- Execute o sistema com Docker Compose:

docker-compose up -d --build

- Aguarde todos os serviços iniciarem

- Verifique os logs para confirmar que tudo está funcionando:

docker-compose logs app --tail=10
docker-compose logs consumer --tail=10

# Variáveis de Ambiente

RABBITMQ_URL=amqp://guest:guest@rabbitmq:5672/
MONGO_URL=mongodb://mongo:27017/
REDIS_URL=redis://redis:6379/0


# Instruções de Uso e testes
Acessando a Documentação da API
Abra o navegador em: http://localhost:8000/docs

Você verá a interface Swagger com todos os endpoints

POST /corridas - Criar corrida

GET /corridas - Listar corridas

GET /saldo/{motorista} - Ver saldo

GET / ROOT

# Testando os Endpoints:

-- POST /corridas - Criar uma corrida

-- Clique no endpoint POST /corridas

-- Clique em "Try it out"

Cole este JSON de exemplo:

{
  "id_corrida": 8,
  "passageiro": {
    "nome": "Maria",
    "telefone": "21991980333"
  },
  "motorista": {
    "nome": "Caio",
    "nota": 9
  },
  "origem": "Itaipuaçu",
  "destino": "São Paulo",
  "forma_pagamento": "Pix",
  "valor": 100,
  "valor_corrida": 100
}


-- Clique em "Execute"

-- Verifique a resposta - deve retornar status 200 

# Teste - Ver logs:

docker-compose logs consumer --tail=3

# Testes Automatizados

python tests/teste.py          
python tests/teste_completo.py 

# CAPTURA DE TELA DO SISTEMA EM EXECUÇÃO

![Tela 1](./foto1.png)
![Tela 2](./foto 2.png)
