import logging
from .config import Config

def setup_logging():
    Config.ensure_directories()

    logging.basicConfig(
        filename=Config.LOGS / "cadweb.log",
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

    return logging.getLogger("cadweb")
