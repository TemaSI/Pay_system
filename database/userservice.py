from database.models import User, Password, Card
from database import get_db

# Регистрация пользователя
def register_user_db(**kwargs):
    db = next(get_db())
    phone_number = kwargs.get('phone_number')

    # Проверка номера
    checker = db.query(User).filter_by(phone_number).first
    if checker:
        return "Пользователь с таким номером жив"
    # Если ползователя нет в базе то регаем
    new_user = User(**kwargs)
    db.add(new_user)
    db.commit()

    # Создать пароль
    new_user_password = Password(user_id=new_user.user_id, **kwargs)
    db.add(new_user_password)
    db.commit()
    return "Пользователь добавлен в базу данных"
# Проверка пароля
def check_password_db(phone_number, password):
    db = next(get_db())
    checker = db.query(Password).filter_by(phone_number=phone_number, password=password).first()
    if checker and checker.password == password:
        return  checker.user_id
    elif not checker:
        return "Ошибка в номере"
    elif checker.password != password:
        return "Something get wrong"

# Получение информации от пользователя
def get_user_cabinet_db(user_id):
    db = next(get_db())
    checker = db.query(User).filter_by(user_id=user_id).first()

    if checker:
        return checker

    return "Ошибка в данных"



# Получение карты по номеру
def get_user_card_by(phone_number):
    db = next(get_db())
    checker = db.query(Card).filter_by(phone_number=phone_number).first()

    if checker:
        return checker

    return "Ошибка в данных"