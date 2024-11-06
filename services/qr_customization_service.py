from io import BytesIO
from PIL import Image
from fastapi import UploadFile
from segno import QRCode
from services.png_converter_service import PNGConverterService


class QRCustomizationService:
    def customize_with_image(self, qr_code: QRCode, image_path: str) -> QRCode:
        qr_code_with_image = qr_code.overlay(image_path)
        return qr_code_with_image

    def customize_with_centered_image(self, out: BytesIO, file_type: str, center_image_binary: UploadFile) -> BytesIO:
        result_out = BytesIO()
        png_converter = PNGConverterService()
        out.seek(0)  # Important to let Pillow load the PNG
        img = Image.open(out)
        img = img.convert('RGB')  # Ensure colors for the output
        img_width, img_height = img.size

        logo_max_size = img_height // 3  # May use a fixed value as well
        center_image = png_converter.convert(center_image_binary)

        # Resize the logo to logo_max_size
        center_image.thumbnail((logo_max_size, logo_max_size), Image.Resampling.LANCZOS)
        # Calculate the center of the QR code
        box = ((img_width - center_image.size[0]) // 2, (img_height - center_image.size[1]) // 2)
        img.paste(center_image, box)
        img.save(result_out, format=file_type)
        result_out.seek(0)
        return result_out
