#  Aplikacja auiz - "Capitals"
Quiz polegający na dopasowaniu kraju do stolicy i stolicy do kraju.

## Cel projektu
Quiz daje możliwość sprawdzenia swojej wiedzy zarówno nt nazwy danego państwa jak i nazwy jego stolicy.
Aby rozpocząć quiz należy założyć konto lub sie zalogować. Na stronie powitalnej, po kliknięciu
 w link z danym rodzajem pytania, przechodzimy na stronę z konkretnym pytaniem oraz trzema odpowiedziami.
 Widoczne są również dwa przyciski: „Pokaż odpowiedź” który przenosi nas do strony z poprawną odpowiedzią
 oraz „Wybierz rodzaj pytania” który przenosi nas do strony wyboru rodzaju pytania.
 Odświeżenie strony z pytaniem powoduje wylosowanie kolejnego kraju (stolicy) oraz zestawu odpowiedzi.

## Użyte technologie
- Python (wersja 3.11)
- Django (wersj 4.2)
- csv editor (wersja 4.53)
- mysql.connector (wersja 8.0.33)
- mysqlclient (wersja 2.1.1)
- systemu kontroli wersji - GIT (wersja 2.41.0)
- IDE - PyCharm w wersji 20231.1.2

## Uruchomienie
Aby uruchomić aplikację "Capitals" należy zainstalować powyższe technologie oraz przeglądarkę internetową

## Pomysły na rozwój projektu
Aplikacja internetowa „Capitals” może być rozwijana w kilku kierunkach takich jak np.:
-	dodanie numeracji pytań (np od 1 do 5 lub 1 - 10)
-	dodanie punktacji oraz końcowego sumowania otrzymanych punktów (np. za każdą dobrą odpowiedź użytkownik otrzymuje 1 punkt)
-	dodanie na stronie powitalnej trzeciego rodzaju pytania – pomieszane pytania o kraj i stolicę
-	pojawianie się odpowiedzi bez przekierowania na inną stronę – użycie technologi AJAX
