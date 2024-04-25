from fastapi import APIRouter

from card import CardAddModel
# допишите все импорты
from database.cardservice import get_exact_card_db


card_router = APIRouter(prefix='/card', tags=['Работа с картами'])


# запрос на добавление карты
@card_router.post('/add')
async def add_new_card(data: CardAddModel):
    # Переводим пайдентик на обычный словарь
    card_data = data.model_dump()
    # и пишем дальше


# запрос на получение информации об определенной карте определенного пользователя
@card_router.get('/exact-card-info')
async def get_card_info(card_id: int, user_id: int):
    pass

# Запрос на получение всех карт пользователя
@card_router.get('/get-info')
async def get_all_user_cards(user_id: int):
    pass


# запрос на удаление карты
@card_router.delete('/delete-card')
async def delete_exact_card(card_id: int):
    pass