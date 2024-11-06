from pydantic import BaseModel


class WifiType(BaseModel):
    ssid: str
    password: str | None
    security: str | None
    hidden: bool = False
