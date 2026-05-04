from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

class PlateResponse(BaseModel):
    numPlaca: str
    marca: Optional[str] = None
    modelo: Optional[str] = None
    color: Optional[str] = None
    anioFabricacion: Optional[int] = None
    propietario: Optional[str] = None
    estado: Optional[str] = None
    fechaRegistro: Optional[datetime] = None
    observaciones: Optional[str] = None
    response: str
    status: str

    model_config = {
        "from_attributes": True
    }

    @classmethod
    def error(cls, numero: str, mensaje: str, status_str: str) -> PlateResponse:
        return cls(
            numPlaca=numero,
            response=mensaje,
            status=status_str,
        )