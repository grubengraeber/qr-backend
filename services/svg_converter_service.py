from wand.image import Image
from io import BytesIO


class SVGConverterService:
    def convert_svg_to_png(self, svg_data: str) -> BytesIO:
        png_io = BytesIO()
        # Load SVG and convert to PNG using wand
        with Image(blob=svg_data.encode("utf-8"), format="svg") as img:
            img.format = 'png'
            img.save(png_io)
        png_io.seek(0)
        return png_io
