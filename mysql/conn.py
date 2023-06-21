import os
import mysql.connector
from mysql.connector import Error
import pandas as pd

# RDS Endpoint
HOST="database-1.cluster-cl1bwfxhbgy4.ap-northeast-2.rds.amazonaws.com"
# Get environment variables
# Default admin,bsd0705!
USER = os.getenv('DB_USER') or "admin"
PASSWORD = os.environ.get('DB_PASSWORD') or "bsd0705!"

## Connect DataBase
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

## Query send
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("complate Query")
    except Error as err:
        print(f"Error: '{err}'")

## Main
if __name__ == "__main__":
    ## 연결
    conn = create_server_connection(HOST,USER,PASSWORD)