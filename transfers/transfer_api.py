from fastapi import APIRouter

from datetime import datetime
# допишите все необходимые импорты
from database.transferservice import create_transaction_db
# валидаторы пайдентик в инит
from transfers import CreateTransactionModel, CancelTransactionModel

transaction_router = APIRouter(prefix='/transaction', tags=['Работа с платежами'])


# Запрос на создание транзакции
@transaction_router.post('/create')
async def add_new_transaction(data: CreateTransactionModel):
    # Переводим пайдентик на обычный словарь
    transaction_data = data.model_dump()
    pass


# Запрос на отмену транзакции
@transaction_router.post('/cancel')
async def cancel_transaction(data: CancelTransactionModel):
    pass


# Запрос на получение всех транзакций определенной карты
@transaction_router.get('/monitoring')
async def get_card_monitoring(card_id: int):
    pass