from backend.core.database import engine, Base
from backend.models import hr_model  # ensure models are imported so Base.metadata knows them

def init_db():
    Base.metadata.create_all(bind=engine)
    print("DB tables created")

if __name__ == "__main__":
    init_db()
