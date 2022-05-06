import psycopg2
from psycopg2 import Error
import csv
print("1 - Show")
print("2 - Update")
print("3 - Insert")
print("4 - Delete")

option = int(input())

if option == 1:
    try: 
        con = psycopg2.connect(
            database="tima",
            host="localhost",
            user="postgres",
            password="Prom2021",
            port="5432"
        )
        cursor = psycopg2.cursor()
        cursor.execute(SELECT * FROM pp2)