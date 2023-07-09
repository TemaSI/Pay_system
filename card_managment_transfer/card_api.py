from main import app
from database import add_user_card_db, delete_user_card_db, get_exact_user_card_db,transfer_money_db, get_all_cards_or_exact_transaction

from datetime import datetime
import random

otp_test = {} # Временное решение
# Добавление карты
@app.post('/add-user-card')
async def add_user_card_api(user_id: int, card_number: int, cardholder: str, card_name: str, card_holder: str, exp_date: int, otp: int):
    if otp_test.get(user_id) == otp:
        result = add_user_card_db( user_id=user_id, cardholder=cardholder, card_name=card_name,
                                card_number=card_number, exp_date=exp_date, added_data=datetime.now(),
                                balance=0)
    else:
        result = "Невреный код"
    return {'status': 1, "message": result}

# Генерация проверочного кода
@app.get('/one-time-password')
async def get_one_time_password(transfer_id: int = 0, user_id: int = 0):
    # Генерим рандомный код
    otp = random.randint(1000, 9999)

    if transfer_id != 0:
        otp_test[transfer_id] = random.randint(1000, 9999)

    elif user_id != 0:
        otp_test[user_id] = otp
# Перевод денег
@app.post('/transfer-user-money')
async def transfer_money_api(card_from: int, card_to: int, otp: int, amount):
    result = transfer_money_db(card_from, card_to, datetime.now(), amount)
    return {'status': 1, 'message': result}

# Удаление карты
@app.delete('/delete-user_card')
async def delete_user_card(card_id: int):
    result = delete_user_card_db(card_id)

    return {'status': 1, 'message': result}

# Вывод карты
@app.get('/get-user-card')
async def get_exact_or_all_cards(user_id: int, card: int = 0):
    result = get_exact_user_card_db(user_id, card)

    return {'status': 1, 'message': result}

# Вывод истории карты
@app.get('/get-user-card')
async def get_exact_card_monitoring(user_id:int, card: int = 0):
    result = get_all_cards_or_exact_transaction(user_id, card)

    return {'status': 1, 'message': result}
