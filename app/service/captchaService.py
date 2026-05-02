import httpx
import logging
from app.config.dbConfig import settings
from app.service.dtos.cloudflareCaptchaResponse import CaptchaResponse

log = logging.getLogger(__name__)

class CaptchaService:
    def __init__(self):
        self.secret_key = settings.CLOUDFLARE_SECRET_KEY
        self.captcha_url = "https://challenges.cloudflare.com/turnstile/v0/siteverify"

    def verify_captcha(self, token: str):
        try:
            with httpx.Client() as client:
                response = client.post(
                    self.captcha_url,
                    data = {
                        "secret": self.secret_key,
                        "response": token,
                    }
                )

                response.raise_for_status()

                json_data = response.json()
                data = CaptchaResponse.model_validate(json_data)

                return data.success

        except Exception as e:
            log.error(f"Error verifying captcha: {str(e)}")
            return False