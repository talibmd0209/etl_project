from src.etl_project.logger import logging
try:
    import yaml
except ImportError:
    raise ImportError("PyYAML module not found. Install it using: pip install PyYAML")
def load_config():
    with open("configs/config.yaml", "r") as f:
        config = yaml.safe_load(f)
        logging.info("Configuration loaded successfully.")
    return config