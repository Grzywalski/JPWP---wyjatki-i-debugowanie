#
# Budujesz moduł do walidacji danych wejściowych formularza.
# Walidacja może napotkać wiele błędów jednocześnie (np. zły
# format e-mail I za krótkie hasło)
#
# Polecenia:
#   1. Stwórz bazową klasę wyjątku `ValidationError` dziedziczącą
#      po `Exception`, która przechowuje pole `field` (nazwa pola)
#      oraz `reason` (powód błędu).
#   2. Stwórz dwie klasy pochodne: `EmailValidationError`
#      i `PasswordValidationError`.
#   3. Uzupełnij funkcję `validate_form` tak, aby:
#      a) zbierała błędy do listy,
#      b) rzucała `ExceptionGroup("Błędy walidacji", [lista błędów])`.
#   4. W bloku `except*` obsłuż każdy typ błędu osobno i wypisz
#      szczegóły (pole + powód).
#   5. WAŻNE: Przy tworzeniu wyjątków użyj `raise ... from original_exc`
#      (exception chaining), aby ukryć wewnętrzną przyczynę przed
#      użytkownikiem, ale zachować ją w `__cause__`.
# 
 
# --- UZUPEŁNIJ: definicje klas wyjątków ---
 
# class ValidationError(...):
#     ...
 
# class EmailValidationError(...):
#     ...
 
# class PasswordValidationError(...):
#     ...
 
# --- KONIEC DEFINICJI KLAS ---
 
 
def _check_email(email: str) -> None:
    """Rzuca wyjątek, jeśli e-mail nie zawiera znaku '@'."""
    try:
        if "@" not in email:
            raise ValueError("Brak znaku @ w adresie e-mail")
    except ValueError as e:
        # --- UZUPEŁNIJ: rzuć EmailValidationError z chainowaniem ---
        pass
 
 
def _check_password(password: str) -> None:
    """Rzuca wyjątek, jeśli hasło ma mniej niż 8 znaków."""
    try:
        if len(password) < 8:
            raise ValueError("Hasło jest za krótkie")
    except ValueError as e:
        # --- UZUPEŁNIJ: rzuć PasswordValidationError z chainowaniem ---
        pass
 
 
def validate_form(email: str, password: str) -> None:
    errors = []
 
    for check in [lambda: _check_email(email), lambda: _check_password(password)]:
        try:
            check()
        except Exception as e:
            errors.append(e)
 
    if errors:
        # --- UZUPEŁNIJ: rzuć ExceptionGroup ---
        pass
 
 
# TESTOWANIE
 
print("=== Test : oba pola błędne ===")
try:
    validate_form("niepoprawny-email", "123")
except* EmailValidationError as eg:
    for exc in eg.exceptions:
        print(f"  Email pole: '{exc.field}', powód: '{exc.reason}'")
        print(f"  Ukryta przyczyna (__cause__): {exc.__cause__}")
except* PasswordValidationError as eg:
    for exc in eg.exceptions:
        print(f"  Hasło pole: '{exc.field}', powód: '{exc.reason}'")
        print(f"  Ukryta przyczyna (__cause__): {exc.__cause__}")
 
print("\n=== Test : tylko błędny e-mail ===")
try:
    validate_form("zly-email", "poprawnehaslo123")
except* EmailValidationError as eg:
    for exc in eg.exceptions:
        print(f"  Email {exc.reason}")
except* PasswordValidationError as eg:
    for exc in eg.exceptions:
        print(f"  Hasło {exc.reason}")
 
print("\n=== Test : poprawne dane (brak wyjątku) ===")
try:
    validate_form("user@example.com", "bezpiecznehaslo")
    print("  Walidacja przeszła pomyślnie.")
except* ValidationError as eg:
    print(f"  Nieoczekiwany błąd: {eg}")