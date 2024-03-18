from sqlalchemy.orm import Session
from models.models import Base, Enterprise, Product
from database import SessionLocal, engine

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

def create_test_data(db: Session):
    if db.query(Enterprise).first() is not None:
        print("Data already exists. Skipping test data creation.")
        return
    
    enterprises = [
        Enterprise(name="Оружейный Концерн 'Калашников'", description="Лидирующий производитель стрелкового и автоматического оружия", location="Москва"),
        Enterprise(name="Бронетанковый Завод 'Уралвагонзавод'", description="Крупнейший производитель бронетехники в России", location="Нижний Тагил"),
        Enterprise(name="Танкостроительный Завод 'Харьковский Тракторный Завод'", description="Производитель боевых танков и бронированных машин", location="Харьков"),
        Enterprise(name="Оборонный Концерн 'Локхид Мартин'", description="Крупнейший производитель военной техники и оборонных систем", location="США"),
    ]
    db.add_all(enterprises)
    db.commit()

    products = [
        Product(name="Автомат Калашникова АК-47", description="Известный во всем мире автоматический пистолет", price=500.0, quantity_in_stock=1000, enterprise_id=1),
        Product(name="Танк Т-90", description="Современный боевой танк с мощным вооружением", price=1000000.0, quantity_in_stock=50, enterprise_id=2),
        Product(name="БМП-3", description="Боевая машина пехоты с мощным вооружением и броней", price=700000.0, quantity_in_stock=100, enterprise_id=2),
        Product(name="Танк Т-84 'Оплот'", description="Украинский танк с высоким уровнем защиты и маневренности", price=1500000.0, quantity_in_stock=30, enterprise_id=3),
        Product(name="F-35 Лайтнинг II", description="Многоцелевой истребитель-бомбардировщик пятого поколения", price=85000000.0, quantity_in_stock=10, enterprise_id=4),
        Product(name="Patriot PAC-3", description="Зенитный ракетный комплекс для защиты от воздушных целей", price=150000000.0, quantity_in_stock=5, enterprise_id=4),
    ]
    db.add_all(products)
    db.commit()

if __name__ == "__main__":
    db = SessionLocal()

    create_test_data(db)

    db.close()
