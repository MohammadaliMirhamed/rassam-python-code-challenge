from classes.database.PostgresDB import PostgresDB
import os
from dotenv import load_dotenv

def main():
    # load the .env file
    load_dotenv()

    # define a database dict
    db_config = {
        'host': os.getenv("POSTGRES_DB_HOST"),
        'user': os.getenv("POSTGRES_DB_USER"),
        'password': os.getenv("POSTGRES_DB_PASSWORD"),
        'port': os.getenv("POSTGRES_DB_PORT"),
        'dbname': os.getenv("POSTGRES_DB_NAME")
    }

    # create a database object
    return PostgresDB(db_config)

db = main();
