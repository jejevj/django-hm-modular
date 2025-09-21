import base64
from io import BytesIO
from barcode import Code128
from barcode.writer import ImageWriter

def generate_barcode_base64(value: str) -> str:
    buffer = BytesIO()
    barcode = Code128(value, writer=ImageWriter())
    barcode.write(buffer)
    return base64.b64encode(buffer.getvalue()).decode()
