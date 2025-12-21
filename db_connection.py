import mysql.connector
from sqlalchemy import create_engine

def get_connection():
    engine = create_engine(
        "mysql+pymysql://root:Sahithi#166@localhost:3306/bank_risk"
    )
    return engine
def get_connection1():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sahithi#166",
        database="bank_risk"
    )

