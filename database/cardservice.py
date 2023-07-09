from database.models import Card, User, Transaction
from database import get_db

# Добавить карту в базу
def add_user_card_db(**kwargs):
    db=next(get_db())
    card_number = kwargs.get('card_number')

    # Проверка была ли добавлена карта
    checker = db.query(Card).filter_by(card_number=card_number).first()

    if checker:
        return "Карта есть в базе"

    new_card = Card(**kwargs)
    db.add(new_card)
    db.commit()

    return "Карта усппешно добавлена"

# Удалить карту из сервиса
def delete_user_card_db(card_id):
    db = next(get_db())
    card = db.query(Card).filter_by(card_id=card_id).first()
    db.delete(card)
    db.commit()
    return "Карта удалена"


# Получить все карты по номеру телефона
def get_user_cards_by_phone_number_db(phone_number):
    db = next(get_db())
    checker = db.query(Card).filter(User.phone_number == phone_number).all()
    return


# Получить определённую карту
def get_exact_user_card_db(user_id, card_id):
    db = next(get_db())
    if card_id == 0:
        card_data = db.query(Card).filter_by(user_id=user_id).all()

    else:
        card_data = db.query(Card).filter_by(user_id=user_id, card_id=card_id).first()

    return card_data
# Получить все транзакции по определённой карте или по всем
def get_all_cards_or_exact_transaction(user_id, card_id):
    db = next(get_db())
    if card_id == 0:
        card_monitor = db.query(Transaction).filter_by(user_id=user_id).all()
    else:
        card_monitor = db.query(Transaction).filter_by(user_id=user_id, card_id=card_id).all()

    db.add(card_monitor)
    db.commit()