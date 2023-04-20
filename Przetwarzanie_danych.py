import csv
import mysql.connector
# import json

with mysql.connector.connect(user='root', password='admin', host='localhost', database='filip') as connection:
    cursor = connection.cursor()

    with open('worldcities.csv', encoding='utf-8') as f:
        reading = csv.DictReader(f)

        for row in reading:
            sql = f"""INSERT INTO
            c_c(country)
            VALUES('{row["country"]}');
            """
            cursor.execute(sql)

        connection.commit()
