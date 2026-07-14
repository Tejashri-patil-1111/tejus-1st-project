import os
import sys
import pandas as pd
import pymysql
# from dotenv import load_dotenv
import dotenv


from src.e2e_ml_project.exception import CustomException
from src.e2e_ml_project.logger import logging

dotenv.load_dotenv()  # Load environment variables from .env file

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')

def read_sql_data():
    logging.info("Reading data from mysql database")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=str(password),
            database=db
        ) # type: ignore
        logging.info('connection Established')
        df = pd.read_sql_query('SELECT * FROM students', mydb)
        print(df.head())
        return df

    except Exception as ex:
        raise CustomException(ex, sys) from ex