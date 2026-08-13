import logging

logging.basicConfig(
    filename="executive_ai.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("ExecutiveAI")

from utils.logger import logger

logger.info("Revenue analysis started")
logger.error("Unable to compute margin")

