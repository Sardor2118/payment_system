from datetime import datetime
from database.models import User
from database import get_db

# register user

def register_user_db(id, username, surname, user_photo, phone_number, email, county, password, reg_date):
    db = next(get_db())
    checker = check_user_email()
    if checker:
        new_user = User(id=id, username=username, surname=surname, user_photo=user_photo, phone_number=phone_number,
                        email=email, county=county, password=password, reg_date=datetime.now())
        db.add(new_user)
        db.commit()
        return new_user.id
    else:
        return "Ошибка, такой Мейл уже занят"


# get information about user

def get_exact_user_db(phone_number, email):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number,
                                       email=email).first()
    if checker:
        return checker
    return "Пользователь не найден"


def check_user_email():
    db = next(get_db())
    checker = db.query(User.email)
    if checker:
        return False
    return True


def edit_user_db(user_id, changeable_info, new_data):
    db = next(get_db())
    all_info = db.query(User).filter_by(id=user_id).first()
    if all_info:
        if changeable_info == "email":
            all_info.email = new_data
        elif changeable_info == "phone_number":
            all_info.phone_number = new_data
        elif changeable_info == "password":
            all_info.password = new_data
        db.commit()
        return "Данные успешно изменены"
    return "Пользователь не найден"


def delete_user_db(user_id):
    db = next(get_db())
    all_info = db.query(User).filter_by(id=user_id).first()
    if all_info:
        db.delete(all_info)
        db.commit
        return "Пользователь удален"
    return 'Пользователь не найден'