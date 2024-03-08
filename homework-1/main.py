"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv

connect = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='1234'
)

with connect:
    with connect.cursor() as cursor:
        with open('north_data/employees_data.csv', 'r') as file:
            data = csv.reader(file)
            next(data)
            for row in data:
                cursor.execute(
                    "insert into emploees (employee_id, first_name, last_name, title, birth_dat, notes) values (%s, %s, %s, %s, %s, %s)",
                    row)

with connect:
    with connect.cursor() as cursor:
        with open('north_data/customers_data.csv', 'r') as file:
            data = csv.reader(file)
            next(data)
            for row in data:
                cursor.execute("insert into customers (customer_id, company_name, contact_name) values (%s, %s, %s)",
                               row)

with connect:
    with connect.cursor() as cursor:
        with open('north_data/orders_data.csv', 'r') as file:
            data = csv.reader(file)
            next(data)
            for row in data:
                cursor.execute(
                    "insert into orders (order_id, customer_id, employee_id, order_date, ship_city) values (%s, %s, %s, %s, %s)",
                    row)

connect.close()
