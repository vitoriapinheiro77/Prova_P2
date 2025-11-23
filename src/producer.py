from faststream.rabbit import RabbitBroker


broker = RabbitBroker("amqp://guest:guest@rabbitmq:5672/")

async def publish_corrida(data: dict):
    """Publica uma mensagem na fila 'corrida_finalizada'."""
    
    async with broker:
        await broker.publish(
            message=data,
            queue="corrida_finalizada"  
        )