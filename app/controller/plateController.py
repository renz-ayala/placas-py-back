from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.config.session import get_db
from app.controller.dtos.plateRequest import PlateRequest
from app.controller.dtos.plateResponse import PlateResponse
from app.service.captchaService import CaptchaService
from app.service.plateService import PlateService

router = APIRouter(prefix="/placas")

@router.post("/verificar")
def verify(plate: PlateRequest, db: Session = Depends(get_db)):

    plate_service = PlateService(db)
    captcha_service = CaptchaService()

    if not captcha_service.verify_captcha(plate.idTransaction):
        response = PlateResponse(
            numPlaca = plate.numPlaca,
            response="El captcha es inválido/expirado",
            status="BAD_REQUEST"
        )
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = response.model_dump(by_alias=True, mode="json")
        )

    result = plate_service.get_plate_data(plate.numPlaca)
    status_map = {
        "OK": status.HTTP_200_OK,
        "NOT_FOUND": status.HTTP_404_NOT_FOUND,
        "BAD_REQUEST": status.HTTP_400_BAD_REQUEST,
        "INTERNAL_SERVER_ERROR": status.HTTP_500_INTERNAL_SERVER_ERROR
    }
    http_status = status_map.get(result.status, status.HTTP_500_INTERNAL_SERVER_ERROR)
    return JSONResponse(
        status_code = http_status,
        content=result.model_dump(by_alias=True, mode="json")
    )