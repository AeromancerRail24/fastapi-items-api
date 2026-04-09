from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Runtime settings for the FastAPI project."""

    app_name: str = "ZNXCpxmf"
    version: str = "0.1.0"
