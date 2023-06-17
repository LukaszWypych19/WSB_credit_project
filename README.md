#  Aplikacja quiz - "Capitals"
Quiz polegający na dopasowaniu kraju do stolicy i stolicy do kraju.

## Cel projektu
Quiz daje możliwość sprawdzenia swojej wiedzy zarówno nt. nazwy danego państwa jak i nazwy jego stolicy. 
Po kliknięciu w link z danym rodzajem pytania, przechodzimy na stronę z konkretnym pytaniem oraz trzema 
odpowiedziami. Widoczne są również dwa przyciski: „Pokaż odpowiedź” który przenosi nas do strony z poprawną
odpowiedzią i możliwością zapisania udzielonej odpowiedzi (przycisk „zapisz odpowiedź – zapisuje odpowiedź
i przenosi nas na stronę z historycznymi odpowiedziami danego użytkownika) oraz „Wybierz rodzaj pytania” 
który przenosi nas do strony wyboru rodzaju pytania. Odświeżenie strony z pytaniem powoduje wylosowanie 
kolejnego kraju (lub stolicy) oraz zestawu odpowiedzi. 

## Użyte technologie
- Python (wersja 3.11)
- Django (wersj 4.2)
- csv editor (wersja 4.53)
- mysql.connector (wersja 8.0.33)
- mysqlclient (wersja 2.1.1)
- systemu kontroli wersji - GIT (wersja 2.41.0)
- IDE - PyCharm w wersji 20231.1.2

## Uruchomienie
Aby uruchomić aplikację należy:
- zainstalować Pythona w wersji 3.11
- zainstalować menedżera zależności Poetry w wersji 1.5.1
- ściągnąć aplikację quiz np. z GitHub (https://github.com/LukaszWypych19/projekt_zaliczeniowy_WSB)
- otworzyć wiersz poleceń i przejść do głównego katalogu ściągniętej aplikacji, następnie wpisać polecenie poetry install aby zainstalować wszystkie potrzebne paczki i zależnosci między nimi
- po zakończeniu instalacji, w wierszu poleceń należy wpisać polecenie poetry run python manage.py runserver
- otworzyć dowolną przeglądarke i wpisać adres 127.0.0.1:8000

## Pomysły na rozwój projektu
Aplikacja internetowa „Capitals” może być rozwijana w kilku kierunkach takich jak np.:
-	dodanie numeracji pytań (np od 1 do 5 lub 1 - 10)
-	dodanie punktacji oraz końcowego sumowania otrzymanych punktów (np. za każdą dobrą odpowiedź użytkownik otrzymuje 1 punkt)
-	dodanie na stronie powitalnej trzeciego rodzaju pytania – pomieszane pytania o kraj i stolicę
-	pojawianie się odpowiedzi bez przekierowania na inną stronę – użycie technologi AJAX
