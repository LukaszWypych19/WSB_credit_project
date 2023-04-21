import csv
# import mysql.connector
# import json

# with mysql.connector.connect(user='root', password='admin', host='localhost', database='filip') as connection:
#     cursor = connection.cursor()

with open('worldcities.csv', encoding='utf-8') as f:
    reading = csv.DictReader(f)

    for row in reading:
        city_name = row['city_ascii'].replace("'", " ")


        # sql = f"""INSERT INTO
        # c_c(capital)
        # VALUES('{row["city_ascii"]}');
        # """
        #     cursor.execute(sql)
        #
        # connection.commit()