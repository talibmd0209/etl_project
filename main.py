from src.etl_project.configs import load_config
from src.etl_project.reader import load_data

config = load_config()

customer_df, product_df, inventory_df, orders_df, employees_df = load_data(config)