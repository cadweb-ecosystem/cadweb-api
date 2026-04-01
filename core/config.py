import os
from pathlib import Path

class Config:
    """Global cadweb configuration."""

    ROOT = Path(__file__).resolve().parents[2]
    DATA = ROOT / "data"
    LOGS = ROOT / "logs"

    @staticmethod
    def ensure_directories():
        Config.DATA.mkdir(exist_ok=True)
        Config.LOGS.mkdir(exist_ok=True)
