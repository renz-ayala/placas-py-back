from pydantic import BaseModel

class PlateRequest(BaseModel):
    numPlaca: str
    idTransaction: str = None