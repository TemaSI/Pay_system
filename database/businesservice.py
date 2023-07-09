from database.models import Card, User, Transaction, Service, ServiceCategory
from database import get_db

def register_business_category_db(name):
    db=next(get_db())

    new_add = ServiceCategory(category_name=name)

    db.add(new_add)
    db.commit()
    return "Выполнено"

def register_business_db(category_id, name, card_number):
    db = next(get_db())

    new_add = Service(service_category=category_id,
                      service_name=name,
                      service_check=card_number)
    # Проверку доб
    db.add(new_add)
    db.commit()
    return "Выполнено"

def get_business_categories_db(exact_category_id):
    db = next(get_db())

    all_categeories = db.query(ServiceCategory).filter_by(category_id=exact_category_id).all()

    return all_categeories

def get_exact_business_db(service_id, category_id):
    db = next(get_db())

    all_business = db.query(Service).filter_by(service_id=service_id, service_category=category_id)

    return all_business

def delete_business_db(service_id):
    db = next(get_db())

    del_business =  db.query(Service).filter_by(service_id=service_id).first()

    db.delete(del_business)
    db.commit()
    return "Выполнено"

def delete_categories_db(category_id):
    db = next(get_db())

    del_categories = db.query(Service).filter_by(category_id=category_id).first()

    db.delete(del_categories)
    db.commit()
    return "Выполнено"