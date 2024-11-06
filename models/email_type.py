from typing import Iterable

from pydantic import BaseModel


class EmailType(BaseModel):
    to: str | Iterable[str]
    cc: str | Iterable[str] | None = None
    bcc: str | Iterable[str] | None = None
    subject: str | None = None
    body: str | None = None
