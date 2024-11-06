from io import BytesIO
from typing import BinaryIO

import segno
from PIL import ImageFile
from segno import helpers

from models.contact_type import ContactType
from models.email_type import EmailType
from models.wifi_type import WifiType
from services.qr_customization_service import QRCustomizationService


class QRCodeGenerator:
    def generate_qr_code_for_text(self, data: str, file_type: str) -> BytesIO:
        out = BytesIO()
        segno.make(data, error="h").save(out, scale=5, kind=file_type)
        out.seek(0)
        return out

    def generate_qr_code_for_contact(self, contact: ContactType, file_type: str) -> BytesIO:
        out = BytesIO()
        helpers.make_vcard(
            name=contact.name,
            displayname=contact.display_name,
            email=contact.email,
            phone=contact.phone,
            fax=contact.fax,
            videophone=contact.videophone,
            memo=contact.memo,
            nickname=contact.nickname,
            birthday=contact.birthday,
            url=contact.url,
            pobox=contact.po_box,
            street=contact.street,
            city=contact.city,
            region=contact.region,
            zipcode=contact.zipcode,
            country=contact.country,
            org=contact.org,
            lat=contact.lat,
            lng=contact.lng,
            title=contact.title,
            photo_uri=contact.photo_uri,
            cellphone=contact.cell_phone,
            homephone=contact.home_phone,
            workphone=contact.work_phone,
        ).save(out, scale=5, kind=file_type)
        out.seek(0)
        return out

    def generate_qr_code_for_email(self, email: EmailType, file_type: str) -> BytesIO:
        out = BytesIO()
        helpers.make_email(
            to=email.to,
            subject=email.subject,
            body=email.body
        ).save(out, scale=5, kind=file_type)
        out.seek(0)
        return out

    def generate_qr_code_for_wifi(self, wifi: WifiType, file_type: str) -> BytesIO:
        out = BytesIO()
        helpers.make_wifi(
            ssid=wifi.ssid,
            password=wifi.password,
            security=wifi.security,
            hidden=wifi.hidden
        ).save(out, scale=5, kind=file_type)
        out.seek(0)
        return out

    def generate_qr_code_with_centered_image(self, data: str, file_type: str, image: BinaryIO) -> BytesIO:
        customizer = QRCustomizationService()
        out = BytesIO()
        segno.make(data, error="h").save(out, scale=5, kind=file_type)
        out.seek(0)
        qr_code_bytes = customizer.customize_with_centered_image(out, file_type, image)
        return qr_code_bytes
