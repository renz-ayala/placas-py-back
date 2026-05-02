import logging
from datetime import datetime
from fpdf import FPDF
from app.service.plateService import PlateService

log = logging.getLogger(__name__)

class ReportService:
    def __init__(self, db_session):
        self.plate_service = PlateService(db_session)

    def generate_report(self, plate_num: str):
        response = self.plate_service.get_plate_data(plate_num)

        if not response or response.status != "OK":
            raise ValueError("No se encontraron datos para generar el reporte")

        try:
            pdf = FPDF()
            pdf.add_page()

            pdf.set_font("Arial", "B", 16)
            pdf.set_text_color(26, 82, 118)
            pdf.cell(0, 10, "CONSULTA DE PLACAS", align="C", new_x="LMARGIN", new_y="NEXT")
            pdf.ln(5)

            pdf.set_draw_color(26, 82, 118)
            pdf.line(10, pdf.get_y(), 200, pdf.get_y())
            pdf.ln(10)

            def add_section(title):
                pdf.set_font("Arial", "B", 12)
                pdf.set_fill_color(242, 242, 242)
                pdf.set_text_color(0)
                pdf.cell(0, 8, f" {title}", fill=True, new_x="LMARGIN", new_y="NEXT")
                pdf.ln(2)

            def add_row(label, value):
                pdf.set_font("Arial", "B", 10)
                pdf.cell(50, 8, label, border="B")
                pdf.set_font("Arial", "", 10)
                pdf.cell(0, 8, str(value) if value else "---", border="B", new_x="LMARGIN", new_y="NEXT")

            add_section("DETALLES DEL VEHICULO")
            add_row("Número de Placa:", response.numPlaca)
            add_row("Marca:", response.marca)
            add_row("Modelo:", response.modelo)
            add_row("Color:", response.color)
            add_row("Año de Fabricación:", response.anioFabricacion)
            pdf.ln(5)

            add_section("INFORMACIÓN EXTRA")
            add_row("Propietario:", response.propietario)
            add_row("Estado:", response.estado)
            add_row("Fecha de Registro:", response.fechaRegistro)

            pdf.set_y(-20)
            pdf.set_font("Arial", "I", 8)
            pdf.set_text_color(120)
            ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            pdf.cell(0, 10, f"{ahora}", align="C")

            return pdf.output()

        except Exception as ex:
            log.error(f"Error en la generación del reporte: {str(ex)}")
            raise

