from sqlalchemy.orm import Session
from app.repository.entity.plate import Plate
from typing import Optional, cast


class PlateRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_by_numero_placa(self, numero: str) -> Optional[Plate]:
        result = self.db.query(Plate).filter(Plate.numero_placa == numero).first()
        return cast(Optional[Plate], result)
