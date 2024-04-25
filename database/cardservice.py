from datetime import datetime
from database.models import Card
from database import get_db

def add_card_db(user_id, card_number, cvv, exp_date, card_name):
    db = next(get_db())

    checker = check_card_info_db(card_number, card_name)
    add_card = Card(user_id=user_id, card_name=card_name, card_number=card_number,
                    cvv=cvv, exp_date=exp_date, reg_date=datetime.now())
    if checker == False:
        return "Уже есть такой"
    elif checker == True:
        db.add(add_card)
        db.commit()
        return "Карта добавлена"

def delete_exact_card_db(card_number):
    db = next(get_db())
    exact_card = db.query(Card).filter_by(card_number=card_number).first()
    if exact_card:
        db.delete(exact_card)
        db.commit()
        return "Успешно удалено"
    return "Ошибка"
def get_exact_user_card_db(user_id):
    db = next(get_db())
    exact_user_card = db.query(Card).filter_by(user_id=user_id).all()
    if exact_user_card:
        return exact_user_card
    return []

def get_exact_card_db(card_number):
    db = next(get_db())
    exact_card = db.query(Card).filter_by(card_number=card_number).first
    if exact_card:
        return exact_card
    return "Не найдено"


def check_card_info_db(card_number, card_name):
    db = next(get_db())
    checker = db.query(Card).filter_by(card_number=card_number, card_name=card_name).first()
    if checker:
        return False
    return True