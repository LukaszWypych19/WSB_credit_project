import csv
import mysql.connector

# import json

print('Do której bazy danych chcesz wyeksportować dane?')
print('1. Lokalna baza danych')
print('2. Baza danych online')
ktora_baza = int(input('Podaj nr bazy: '))


if ktora_baza == 1:

# lokalna baza danych
    with mysql.connector.connect(user='root', password='admin', host='localhost', database='filip') as connection:
        cursor = connection.cursor()

# czytamy plik csv za pomoca metody dictreader
        with open('worldcities.csv', encoding='utf-8') as f:
            reading = csv.DictReader(f)

            # w kolumnie city_ascii zamieniamy "'" na " "
            for row in reading:
                city_name = row['city_ascii'].replace("'", " ")

                # wybieramy z tabeli tylko te wiersze w ktorych sa stolice czyli w kolumnie capital wpisane jest primary
                # tworzymy listy zawierajace panstwo,miasto i czy jest stolica z kazdego wiersza
                if row['capital'] == 'primary':
                    list_of_c_c = [row['country'], city_name, row['capital']]
                    # print(list_of_c_c)

                    # local database - "filip"
                    sql = f"""INSERT INTO
                    countries_capitals(country, city, capital)
                    VALUES('{list_of_c_c[0]}', '{city_name}', '{list_of_c_c[2]}');
                    """
                    cursor.execute(sql)

                connection.commit()

elif ktora_baza == 2:
# baza danych online - https://www.freemysqlhosting.net
    with mysql.connector.connect(user='sql7614159', password='1zs2QJ8BT1', host='sql7.freemysqlhosting.net',
                                 database='sql7614159') as connection:
        cursor = connection.cursor()

        # czytamy plik csv za pomoca metody dictreader
        with open('worldcities.csv', encoding='utf-8') as f:
            reading = csv.DictReader(f)

            # w kolumnie city_ascii zamieniamy "'" na " "
            for row in reading:
                city_name = row['city_ascii'].replace("'", " ")

                # wybieramy z tabeli tylko te wiersze w ktorych sa stolice czyli w kolumnie capital wpisane jest primary
                # tworzymy listy zawierajace panstwo,miasto i czy jest stolica z kazdego wiersza
                if row['capital'] == 'primary':
                    list_of_c_c = [row['country'], city_name, row['capital']]
                    # print(list_of_c_c)

                    # local database - "filip"
                    sql = f"""INSERT INTO
                    countries_capitals(country, city, capital)
                    VALUES('{list_of_c_c[0]}', '{city_name}', '{list_of_c_c[2]}');
                    """
                    cursor.execute(sql)

                connection.commit()
