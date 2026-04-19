from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Runtime settings for the FastAPI project."""

    app_name: str = "Znxcpxmf API"
    version: str = "0.1.0"
    environment: str = "development"
