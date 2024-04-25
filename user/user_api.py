from fastapi import APIRouter, Depends, HTTPException, Request
from datetime import datetime
from pydantic import BaseModel
#импортируйте все необходимое
from database.userservice import register_user_db, get_exact_user_db, edit_user_db, delete_user_db
# пайдентик валидации из инит
from user import UserRegisterModel, EditUserModel
import re

user_router = APIRouter(prefix='/user', tags=['Работа с пользователем'])

regex = re.compile(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+')


# регистрация пользователя
@user_router.post('/register')
async def register_user(data: UserRegisterModel):
    # переводим пайдентик в обычный словарь
    new_user_data = data.model_dump()
    # проверяем на валидность
    if not regex.match(new_user_data['email']):
        raise HTTPException(status_code=400, detail='Неверный формат email')
    if len(new_user_data['password']) < 8:
        raise HTTPException(status_code=400, detail='Пароль должен быть не менее 8 символов')
    if new_user_data['password']!= new_user_data['confirm_password']:
        raise HTTPException(status_code=400, detail='Пароли не совпадают')
    # проверяем есть ли такой пользователь в базе
    if register_user_db(new_user_data):
        raise HTTPException(status_code=400, detail='Такой пользователь уже существует')
    # добавляем пользователя в базу
    register_user_db(new_user_data)
    # возвращаем информацию о пользователе
    return new_user_data


# Получение информации о пользователе
@user_router.get('/info')
async def get_user(user_id: int):
    exact_user = get_exact_user_db(user_id=user_id)
    return {'status': 1, 'message': exact_user}

# Изменить данные о пользователе
@user_router.put('/edit-data')
async def change_user_profile(user_id: int, changeable_info: str, new_data: str):
    data = edit_user_db(user_id=user_id, changeable_info=changeable_info, new_data=new_data)
    return {'status': 1, 'message': data}

# удалить пользователя
@user_router.delete('/delete-user')
async def delete_user(user_id: int):
    data = delete_user_db(user_id=user_id)
    post_id = data.get('post_id')
    if post_id:
        delete_user_db(user_id)
        return {"status": 1, "message": "Юзер успешно удалён"}
    return {"status": 0, "message": "Ошибка"}