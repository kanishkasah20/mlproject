import os #(so that i can make current path and jo bhi folders and all)
import sys #(for handling Custom exception and logging bhi)
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv('db')

def read_sql_data():
    logging.info("Reading SQL Database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established",mydb)
        df=pd.read_sql_query('Select * from students',mydb)
        print(df.head())

        return df

    except Exception as ex:
        raise CustomException(ex)


