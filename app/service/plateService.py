import re
from fastapi import HTTPException, status
from app.repository.plateRepository import PlateRepository


class PlateService:
    def __init__(self, db_session):
        self.repository = PlateRepository(db_session)
        self.validators = r"^[A-Z0-9Ñ]{6,7}$"

    def get_plate_data(self, numero: str):
        if not numero or not re.match(self.validators, numero):
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "El formato de la placa es inválido"
            )

        try:
            plate = self.repository.find_by_numero_placa(numero.upper().strip())

            if not plate:
                raise HTTPException(
                    status_code = status.HTTP_404_NOT_FOUND,
                    detail = "La placa no existe en los registros"
                )

            plate.response = "Operación correcta"
            plate.status = "OK"

            return plate

        except HTTPException as h:
            return h

        except Exception as ex:
            print(f"Error crítico al consultar placa {numero}:{str(ex)}")
            raise HTTPException(
                status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail = "Hubo un error en la operación"
            )