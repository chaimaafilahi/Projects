# ETL method used for this file
import os
import pandas as pd
import src.common as common
from dotenv import load_dotenv
import psycopg

load_dotenv()
host = os.getenv("host")
dbname = os.getenv("dbname")
user = os.getenv("user")
password = os.getenv("password")
port = os.getenv("port")
def extract_customers():
    df = (common.readfile())
    return df

def transform_customers(df):
    print(df)
    return df


def load_customers(df):
    with psycopg.connect(host=host, dbname=dbname, user=user, password=password, port=port) as conn:
        with conn.cursor() as cur:
            sql = """
            CREATE TABLE customers ( 
            pk_customer character varying PRIMARY KEY,
            region character varying,
            city character varying,
            cap character varying);
                    """
            try:
                cur.execute(sql)
            except psycopg.errors.DuplicateTable as pse:
                print(pse)
                conn.commit()
                request = input("Would you like to delete the table? Y/N").upper()
                if request == "Y":
                    sql_delete ="""
                    DROP TABLE customers;
                    """
                    cur.execute(sql_delete)
                    print("Table deleted")
                    conn.commit()
                    print("Recreate customers table...")
                    cur.execute(sql)

            sql = """
                    INSERT INTO customers
                    (pk_customer, region, city, cap)
                    VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING;
                    """

            common.bar_load(df, cur, sql)
            conn.commit()

def main():
    df = extract_customers()
    df = transform_customers(df)
    load_customers(df)


if __name__ == "__main__":
    main()
