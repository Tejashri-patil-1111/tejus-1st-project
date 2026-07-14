import os   
import sys
from src.e2e_ml_project.exception import CustomException        
from src.e2e_ml_project.logger import logging
import pandas as pd
import pymysql

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    def load_dotenv():
        pass

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')

def read_sql_data():
    logging.info("Reading data from mysql database")    
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        logging.info('connection Established', mydb)
        df=pd.read_sql('SELECT * FROM Students', con=mydb)
        print(df.head())

        return df

        
    except Exception as ex:
        raise CustomException(ex)
