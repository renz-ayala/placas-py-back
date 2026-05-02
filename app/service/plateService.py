import re
from app.controller.dtos.plateResponse import PlateResponse
from app.repository.plateRepository import PlateRepository


class PlateService:
    def __init__(self, db_session):
        self.repository = PlateRepository(db_session)
        self.validators = r"^[A-Z0-9Ñ]{6,7}$"

    def get_plate_data(self, numero: str):
        if not numero or not re.match(self.validators, numero):
            return PlateResponse(
                numPlaca = numero,
                response = "El formato de la placa es inválido",
                status = "BAD_REQUEST"
            )

        try:
            plate = self.repository.find_by_numero_placa(numero.upper().strip())

            if not plate:
                return PlateResponse(
                    numPlaca = numero,
                    response = "La placa no existe en los registros",
                    status = "NOT_FOUND",
                )

            return PlateResponse(
                numPlaca = plate.numero_placa,
                marca = plate.marca,
                modelo = plate.modelo,
                color = plate.color,
                anioFabricacion = int(plate.anio_fabricacion),
                propietario = plate.propietario_dni,
                estado = plate.estado,
                fechaRegistro = plate.fecha_registro,
                observaciones = plate.observaciones,
                response = "Operación Correcta",
                status = "OK",
            )

        except Exception as ex:
            print(f"Error crítico al consultar placa {numero}:{str(ex)}")
            return PlateResponse(
                numPlaca = numero,
                response = "Hubo un error en la operación",
                status = "INTERNAL_SERVER_ERROR"
            )