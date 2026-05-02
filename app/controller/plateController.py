from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.repository.db.session import get_db
from app.controller.dtos.plateRequest import PlateRequest
from app.controller.dtos.plateResponse import PlateResponse
from app.service.plateService import PlateService

router = APIRouter(prefix="/placas")

@router.post("/verificar", response_model=PlateResponse)
def verify(plate: PlateRequest, db: Session = Depends(get_db)) -> PlateResponse:
    plate_service = PlateService(db)
    return plate_service.get_plate_data(plate.numPlaca)