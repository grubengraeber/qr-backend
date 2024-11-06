from models.qr_code_type import QRCodeType
from validators.file_type_validator import FileTypeValidator


class QRCodeTypeValidator:
    def validate(self, qr_code_type: QRCodeType) -> bool:
        file_type_validator = FileTypeValidator()
        file_type_is_valid = file_type_validator.validate(qr_code_type.file_type)
        text_is_not_empty = bool(qr_code_type.text_to_encode)
        return file_type_is_valid and text_is_not_empty
