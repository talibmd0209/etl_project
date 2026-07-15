import pandas as pd
from src.etl_project.logger import logging


def load_data(config):
    try:
        customer_df = pd.read_excel(config["input"]["customer_file"]["path"])
        logging.info("Customer file loaded successfully.")

        product_df = pd.read_excel(config["input"]["products_file"]["path"])
        logging.info("Product file loaded successfully.")

        inventory_df = pd.read_excel(config["input"]["inventory_file"]["path"])
        logging.info("Inventory file loaded successfully.")

        orders_df = pd.read_excel(config["input"]["orders_file"]["path"])
        logging.info("Orders file loaded successfully.")

        employees_df = pd.read_excel(config["input"]["employees_file"]["path"])
        logging.info("Employees file loaded successfully.")
        return customer_df, product_df, inventory_df, orders_df,employees_df

    except FileNotFoundError as e:
        logging.exception("Input file not found.")
        raise

    except Exception as e:
        logging.exception("Unexpected error while loading data.")
        raise