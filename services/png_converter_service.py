import cairosvg
from PIL import Image
from fastapi import UploadFile


class PNGConverterService:
    def convert(self, image: UploadFile) -> Image:
        # check if is svg
        print(image.filename.endswith('.svg'))

        if image.filename.endswith('.svg'):
            converted_png_file = cairosvg.svg2png(file_obj=image)
            return Image.open(converted_png_file)
        result = Image.open(image.file)
        return result
