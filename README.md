# ABwP-Aspekty-bezpieczenstwa-w-programowaniu-semestr-V
Repozytorium z projektem z przedmiotu- Aspekty bezpieczeństwa w programowaniu, semestr V, prowadzący: dr inż. P Bobiński

Projekt przedstawia aplikację webową w Pythonie, która:
1. Zabezpiecza hasła użytkowników za pomocą szyfrowania bcrypt.
2. Pokazuje podatność na atak SQL Injection i implementuje zabezpieczenia przed tym atakiem.

** Technologie
- Python 3.13
- Flask
- SQLite
- Bcrypt

** Funkcjonalności
1. Formularz logowania.
2. Zabezpieczenie haseł użytkowników za pomocą szyfrowania.
3. Ochrona przed SQL Injection przy użyciu przygotowanych zapytań.

** Wymagania 
- Python 3.13
- Zainstalowane biblioteki:
  pip install flask bcrypt

** Problemy napotkane podczas tworzenia projektu:

1- Problem: Brak biblioteki cryptography w systemie

Opis: Podczas implementacji szyfrowania za pomocą algorytmu AES pojawił się błąd ModuleNotFoundError, ponieważ biblioteka cryptography nie była zainstalowana.
Rozwiązanie: Użyłam polecenia:

pip install cryptography

2- Problem: SQL Injection nie działał w pierwszych testach

Opis: Po zaimplementowaniu podatności na SQL Injection i próbie wstrzyknięcia złośliwego zapytania aplikacja zwracała komunikat „Błędny login lub hasło”. Powodem była niepoprawna konfiguracja danych w bazie i zapytania SQL.
Rozwiązanie: Zweryfikowałam dane w bazie i poprawiłam zapytanie SQL, co umożliwiło skuteczną demonstrację podatności.

3- Problem: Porównywanie haseł z użyciem bcrypt zwracało błąd

Opis: Podczas weryfikacji haseł pojawił się błąd AttributeError: 'bytes' object has no attribute 'encode', ponieważ dane z bazy były już zapisane w formacie bytes, a funkcja bcrypt.checkpw próbowała ponownie je zakodować.
Rozwiązanie: Zmieniłam sposób porównywania haseł w kodzie na:

bcrypt.checkpw(password.encode('utf-8'), user[2])

** Working Code-
Dodałam dodatkowo folder "working code" z kodem z poszczegółnych etapów tworzenia projektu, żeby można było zobaczyć jak kod zmieniał się na poszczególnych etapach.

