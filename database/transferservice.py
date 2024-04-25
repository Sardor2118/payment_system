from datetime import datetime
from database.models import Transactions, Card
from database import get_db

# проверка карты
def _validate_card(card_number):
    db = next(get_db())
    card = db.query(Card).filter_by(card_number=card_number).first()
    if card:
        return card
    return False
# создать перевод
def create_transaction_db(card_from, card_to, amount):
    db = next(get_db())
    card_from = _validate_card(card_from)
    card_to = _validate_card(card_to)


    if card_from and card_to:
        if card_from.amount >= amount:
            transfer = Transactions(card_from=card_from.card_number, card_to=card_to.card_number,
                                    amount=amount, transfer_time=datetime.now())
            card_from.card_balance -= amount
            card_to.card_balance += amount
            db.add(transfer)
            db.commit()
            return "Успешно создано"
        return "Недостаточно средств"
    return "Карта не найдена"


# получить все переводы по карты
def get_card_transaction_db(card_number):
    db = next(get_db())
    card_transactions = db.query(Transactions).filter_by(card_from=card_number).all()
    return card_transactions
# отменить перевод
def cancel_tranfser_db(transfer_id):
    db = next(get_db())
    exact_transfer = db.query(Transactions).filter_by(id=transfer_id).first()
    if exact_transfer:
        db.delete(exact_transfer)
        db.commit()
        return "Успешно отменено"
    return "Ошибка"
# удалить перевод
def delete_tranfser_db(transfer_id):
    db = next(get_db())
    exact_transfer = db.query(Transactions).filter_by(id=transfer_id).first()
    if exact_transfer:
        card_to = db.query(Card).filter_by(card_number=exact_transfer.card_to).first()
        card_from = db.query(Card).filter_by(card_number=exact_transfer.card_from).first()
        amount = exact_transfer.amount
        if card_from.amount >= amount:
            card_from.card_balance -= amount
            card_to.card_balance += amount
        db.delete(exact_transfer)
        db.commit()
        return "Успешно удалено"
    return "Ошибка"