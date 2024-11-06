from io import BytesIO
from typing import BinaryIO
from PIL import Image

from services.svg_converter_service import SVGConverterService


class PNGConverterService:
    def convert(self, image: BinaryIO) -> Image:
        if image.name.endswith('.svg'):
            return self.convert_from_svg(image)
        result = Image.open(image)
        return result

    def convert_from_svg(self, svg: BinaryIO) -> Image:
        # Convert SVG to PNG
        svg_converter = SVGConverterService()
        png = svg_converter.convert_svg_to_png(svg.read().decode("utf-8")).getvalue()
        result = Image.open(BytesIO(png))
        return result
