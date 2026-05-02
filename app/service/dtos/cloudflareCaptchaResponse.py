from pydantic import Field, BaseModel
from typing import List, Optional


class CaptchaResponse(BaseModel):
    success: bool
    error_codes: Optional[List[str]] = Field(None, alias="error-codes")
    challenge_ts: Optional[str] = Field(None, alias="challenge_ts")
    hostname: Optional[str] = None

    class Config:
        from_attributes = True
        populate_by_name = True