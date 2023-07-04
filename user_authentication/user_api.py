from main import app


# Регистрация пользователя
@app.post('/register-user')
async def register_user_api(phone_number:int, name:str, pincode:int, password:str):
    pass

# Вход в аккаунт
@app.get('/login')
async def login_user_api(phone_number: int, password: str):
    pass

# Вывод информации пользователя
@app.get('/user-cabinet')
async def get_user_cabinet_api(user_id: int):
    pass

# Получить карты по номеру
@app.get('/det-user-cards')
async def get_user_cards_by_phone_number_api(phone_number: api):
    pass
