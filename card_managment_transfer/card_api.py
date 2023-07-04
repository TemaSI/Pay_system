from main import app

# Добавление карты
@app.post('/add-user-card')
async def add_user_card_api(user_id: int, card_number: int, cardholder: str, card_holder: str, exp_date: int, otp: int):
    pass

# Генерация проверочного кода
@app.get('/one-time-password')
async def get_one_time_password(transfer_id:int):
    pass

# Перевод денег
@app.post('/transfer-user-money')
async def transfer_money_api(card_from: int, card_to: int, otp: int):
    pass

# Удаление карты
@app.delete('/delete-user_card')
async def delete_user_card(card_id: int , user_id: int):
    pass

# Вывод карты
@app.get('/get-user-card')
async def get_exact_or_all_cards(user_id: int, card: int = 0):
    pass

# Вывод истории карты
@app.get('/get-user-card')
async def get_exact_card_monitoring(card: int = 0):
    pass
