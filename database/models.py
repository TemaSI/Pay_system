from database import Base, relationship
from sqlalchemy import Column, Float, Integer, String, Boolean, Date, DateTime, ForeignKey

# Таблица пользователей
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    phone_number = Column(Integer, nullable=False)
    name = Column(String, nullable= False)

    reg_date = Column(DateTime)

# Таблица паролей
class Password(Base):
    __tablename__ = 'user_password'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    password = Column(String, nullable=False)
    pincode = Column(Integer)

    user_fk = relationship(User)
# Таблица карт
class Card(Base):
    __tablename__ = 'user_cards'
    card_id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=True)
    card_number = Column(Integer, nullable=False)
    card_name = Column(String)
    cardholder = Column(String)
    exp_data = Column(Integer, nullable=False)
    balance = Column(Float)
    added_date = Column(DateTime)

    user_fk = relationship(User)

# Таблица платежей
class Transaction(Base):
    __tablename__ = 'user_transactions'
    transaction_id = Column(Integer, autoincrement=True, primary_key=True)
    card_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    amount = Column(Float, nullable=False)
    card_to = Column(Integer, nullable=False)

    card_fk = relationship(User)
# Таблица сервисов
class ServiceCategory(Base):
    __tablename__ = 'service_categories'
    category_id = Column(Integer, autoincrement=True, primary_key=True)
    category_name = Column(String, nullable=False)

    added_date = Column(DateTime)

class Service(Base):
    __tablename__ = 'service'
    service_id=Column(Integer, autoincrement=True, primary_key=True)
    service_category = Column(Integer, ForeignKey('service_categories.category_id'), nullable=False)
    service_name=Column(String, nullable=False)
    service_balance = Column(Float)
    service_check = Column(Integer, nullable=False)

    reg_date = Column(DateTime)

    category_fk = relationship(ServiceCategory)
