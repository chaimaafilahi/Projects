# per usare le funzioni dentro customers.py
import src.customers as c
import src.common as comm
import src.products as p
import src.categories as cg
import src.orders as o
import src.orders_products as op

if __name__ == "__main__":
    response = -1
    while response != 0:
        response = int(input(""" What you want to do?\n
        -1: Run ETL of customers
        -2: Run Integration data of region and city
        -3: Run Format region for PowerBI
        -4: Run ELT of categories
        -5: Run ELT of products
        -6: Run ETL of orders
        -7: Run ETL of orders_products
        -0: Exit \n"""))
        if response == 1:
            df_customers = c.extract()
            df_customers = c.transform(df_customers)
            c.load(df_customers)
        elif response == 2:
            c.integrate_city_region()
        elif response == 3:
            comm.format_region()
        elif response == 4:
            df_categories = cg.extract()
            df_categories = cg.transform(df_categories, "product_category_name_english")
            cg.load(df_categories)
        elif response == 5:
            df_products = p.extract()
            print("First you need to clean the file, for execute ETL")
            df_products = p.raw_load(df_products)
            df_products1 = p.extract()
            df_products1 = p.transform(df_products1)
            p.load(df_products1)
        elif response == 6:
            df_orders = o.extract()
            df_orders = o.transform(df_orders)
            o.load(df_orders)
        elif response == 7:
            df_orders_product = op.extract()
            df_orders_product = op.transform(df_orders_product)
            op.load(df_orders_product)
        else:
            response = 0
