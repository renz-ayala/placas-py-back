from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class PlateResponse(BaseModel):
    numPlaca: str = Field(..., alias="numero_placa")
    marca: Optional[str] = None
    modelo: Optional[str] = None
    color: Optional[str] = None
    anioFabricacion: Optional[int] = Field(None, alias="anio_fabricacion")
    propietario: Optional[str] = Field(None, alias="propietario_dni")
    estado: str
    fechaRegistro: datetime = Field(..., alias="fecha_registro")
    observaciones: Optional[str] = None
    response: str
    status: str

    class Config:
        from_attribute = True
        populated_by_name = True