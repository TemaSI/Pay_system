from main import app


# Регистрация категории бизнеса
@app.post('/register-business-category')
async def register_business_category_api(name: str):
    pass

# Регистрация бизнеса
@app.post('/register-business')
async def register_business(category_id, name: str, card_number: int):
    pass


# Вывод всех категорий
@app.get('/get-all-categories')
async def get_business_categories_api(exact_category_id: int = 0):
    pass

#Вывод всех бизнесов
@app.get('get-business')
async def get_exact_business_api(business_id: int, category_id: int)
    pass

# Оплата услуг
@app.post('/pay-service')
async def pay_for_service(business_id: int, from_card: int, amount: float):
    pass

# Удалить бизнес
@app.delete('/delete-business')
async def delete_business(business_id: int):
    pass

# Удаление категории
@app.delete('/delete-categories')
async def delete_categories(category_id: int):
    pass