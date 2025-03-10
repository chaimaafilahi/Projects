# Pipeline Project
## Company: OlistIT

First we are going ro create directories:
* __data__ : raw, processed, clean for our files 
* **src**
* __file .env-example__ : with personal element for connection with db

Schema of database:

*__CUSTOMERS__*:
* pk_customer (varchar)
* region (varchar)
* city (varchar)
* cap (varchar): format by inserting a 0 in front

*__CATEGORIES__* :
* pk_category (serial)
* name (varchar)

*__PRODUCTS__* :
* pk_product (varchar)
* fk_category (integer)
* name_length (integer)
* description_length (integer)
* imgs_qty (integer)

*__ORDERS__* :
* pk_order (varchar)
* fk_customer (varchar)
* status (varchar)
* purchase_timestamp (timestamp)
* delivered_timestamp (timestamp)
* estimated_date (date)

*__SELLERS__* :
* pk_seller (varchar)
* region (varchar)


*__ORDERS_PRODUCTS__* :
* pk_order_product (serial)
* fk_order (varchar)
* fk_product (varchar)
* fk_seller (varchar)
* price (float)
* freight (float)