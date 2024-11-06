from pydantic import BaseModel


class QRCodeType(BaseModel):
    text_to_encode: str
    file_type: str
