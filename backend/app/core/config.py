from pydantic import BaseSettings

# Settings is used to load environment variables from a .env file
class Settings(BaseSettings):
    DB_HOST: str  # Database host (e.g., localhost)
    DB_PORT: int  # Database port (default: 5432)
    DB_NAME: str  # Database name
    DB_USER: str  # DB username
    DB_PASSWORD: str  # DB password

    SECRET_KEY: str  # JWT secret
    ALGORITHM: str = "HS256"  # JWT algorithm
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Token expiration in minutes

    class Config:
        env_file = ".env"  # Path to .env file for local development

# Global settings instance to be imported elsewhere
settings = Settings()