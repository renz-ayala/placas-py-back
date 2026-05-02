from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, text
from app.repository.db.session import Base

class Plate(Base):
    __tablename__ = 'placa'
    __table_args__ = { "schema":"extranet"}

    id_placa = Column(Integer, primary_key=True, autoincrement=True)
    numero_placa = Column(String(10), nullable=False, unique=True)
    marca = Column(String(50))
    modelo = Column(String(50))
    color = Column(String(30))
    anio_fabricacion = Column(Numeric(4))
    propietario_dni = Column(String(15))
    estado = Column(String(20), server_default="ACTIVO")
    fecha_registro = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    observaciones = Column(String(500))
