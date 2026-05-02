from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "consulta-placas-ms"
    DB_HOST: str = None
    DB_PORT: str = None
    DB_NAME: str = None
    DB_USER: str = None
    DB_PASSWORD: str = None
    SECRET_KEY: str = None
    CLOUDFLARE_SECRET_KEY: str = None

    def database_url(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()