# per usare le funzioni dentro customers.py
import src.customers as c
import src.products as p
import src.categories as cg


if __name__ == "__main__":
    df_customers= c.extract_customers()
    df_customers = c.transform_customers(df_customers)
    c.load_customers(df_customers)
    '''p.extract_products()
    p.transform_products()
    p.load_products()
    cg.extract_categories()
    cg.transform_categories()
    cg.load_categories()'''

