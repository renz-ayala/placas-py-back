from sqlalchemy.orm import Session
from app.repository.entity.plate import Plate


class PlateRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_numero_placa(self, numero: str) -> type[Plate] | None:
        return self.db.query(Plate).filter(Plate.numero_placa == numero).first()
