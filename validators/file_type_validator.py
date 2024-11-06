from models.export_type import ExportType


class FileTypeValidator:
    def validate(self, file_type: str):
        export_types = [export_type.value for export_type in ExportType]
        if file_type not in export_types:
            return False
        return True
