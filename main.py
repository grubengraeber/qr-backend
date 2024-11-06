from io import BytesIO
from fastapi.responses import StreamingResponse
from models.export_type import ExportType
from models.qr_code_type import QRCodeType
from services.qr_service import QRCodeGenerator
from fastapi import FastAPI, Response, UploadFile
from validators.qr_code_type_validator import QRCodeTypeValidator

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/qr-codes/classic")
def read_item(qr_code_type: QRCodeType):
    qr_code_type_validator = QRCodeTypeValidator()
    if not qr_code_type_validator.validate(qr_code_type):
        export_types = str.join(", ", [export_type.value for export_type in ExportType])
        message = f"Invalid data type. Supported types are {export_types}. Text must not be empty."
        return Response(
            status_code=400, content=message
        )
    file_type: str = qr_code_type.file_type

    qr_code_generator = QRCodeGenerator()
    qr_code_bytes: BytesIO = qr_code_generator.generate_qr_code_for_text(qr_code_type.text_to_encode, file_type)

    media_type = f"image/{file_type}" if file_type != ExportType.PDF else "application/pdf"

    return StreamingResponse(
        content=qr_code_bytes,
        media_type=media_type
    )


@app.post("/qr-codes/custom/{text}")
def read_item(text: str, file: UploadFile):
    print(file)
    if not text:
        return Response(status_code=400, content="Text must not be empty.")

    qr_code_type = QRCodeType(text_to_encode=text, file_type=ExportType.PNG.value)

    qr_code_generator = QRCodeGenerator()
    qr_code_bytes: BytesIO = qr_code_generator.generate_qr_code_with_centered_image(
        qr_code_type.text_to_encode,
        qr_code_type.file_type,
        file
    )

    return StreamingResponse(
        content=qr_code_bytes,
        media_type="image/png"
    )
