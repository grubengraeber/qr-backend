from datetime import date
from typing import Iterable
from pydantic import BaseModel


class ContactType(BaseModel):
    name: str
    display_name: str
    email: str | Iterable[str] | None = None
    phone: str | Iterable[str] | None = None
    fax: str | Iterable[str] | None = None
    videophone: str | Iterable[str] | None = None
    memo: str | None = None
    nickname: str | None = None
    birthday: str | date | None = None
    url: str | Iterable[str] | None = None
    po_box: str | None = None
    street: str | None = None
    city: str | None = None
    region: str | None = None
    zipcode: str | None = None
    country: str | None = None
    org: str | None = None
    lat: float | None = None
    lng: float | None = None
    title: str | Iterable[str] | None = None
    photo_uri: str | Iterable[str] | None = None
    cell_phone: str | Iterable[str] | None = None
    home_phone: str | Iterable[str] | None = None
    work_phone: str | Iterable[str] | None = None
