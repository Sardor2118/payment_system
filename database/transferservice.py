from datetime import datetime
from database.models import Transaction, Card
from database import get_db


# проверка карты
def _validate_card(card_number):
    db = next(get_db())
    card = db.query(Card).filter_by(card_number=card_number).first()
    if card:
        return True
    return False
# создать перевод
def create_transaction_db(card_from, card_to, amount, datetime, card_number):
    db = next(get_db())
    card_from = db.query(Card).filter_by(card_number=card_from).first()
    card_to = db.query(Card).filter_by(card_number=card_to).first()
    card = db.query(Card).filter_by(card_number=card_number).first()
    if card:
        if card_from and card_to:
            transfer = Transaction(card_from=card_from.card_number, card_to=card_to.card_number, amount=amount,
                                   date=datetime.now())
            db.add(transfer)
            db.commit()
            return "Успешно создано"
        return "Ошибка"
        return False
    elif card.amount >= amount:
        return True
    return False

# получить все переводы по карты
def get_card_transaction_db(card_number):
    db = next(get_db())
    card_transactions = db.query(Transaction).filter_by(card_from=card_number).all()
    return card_transactions
# отменить перевод
def cancel_tranfser_db(transfer_id):
    db = next(get_db())
    exact_transfer = db.query(Transaction).filter_by(id=transfer_id).first()
    if exact_transfer:
        db.delete(exact_transfer)
        db.commit()
        return "Успешно отменено"
    return "Ошибка"
# удалить перевод
def delete_tranfser_db(transfer_id):
    db = next(get_db())
    exact_transfer = db.query(Transaction).filter_by(id=transfer_id).first()
    if exact_transfer:
        db.delete(exact_transfer)
        db.commit()
        return "Успешно удалено"
    return "Ошибка"


