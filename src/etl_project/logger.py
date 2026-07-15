import logging
import os
from datetime import datetime

# Create logs directory
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Log file name
log_file = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Full path to log file
log_file_path = os.path.join(log_dir, log_file)

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s"
)

