#
# Piszesz narzędzie do tymczasowego przekierowania logów
# aplikacji do pliku (zamiast na konsolę). Po zakończeniu bloku
# `with` logi mają wracać na standardowe wyjście.
#
# Twoje zadanie:
#   1. Zaimplementuj klasę `LogRedirector` jako context manager
#      (metody `__enter__` i `__exit__`).
#      - `__enter__`: otwiera plik `log_path` do zapisu i przekierowuje
#        `sys.stdout` na ten plik; zwraca obiekt pliku.
#      - `__exit__`: przywraca `sys.stdout`, zamyka plik.
#        Obsłuż ewentualny wyjątek wewnątrz bloku `with` –
#        wypisz na ORYGINALNYM stdout komunikat
#        "Błąd wewnątrz bloku with: <wyjątek>" i zwróć False
#        (wyjątek ma się propagować dalej).
#   2. Użyj `LogRedirector` w bloku `with` i wykonaj kilka wywołań
#      `print(...)` – powinny trafić do pliku, nie na konsolę.
#   3. Po wyjściu z bloku `with` zweryfikuj, że `sys.stdout`
#      znów jest konsolą (wypisz potwierdzenie).
#
 
import sys
 
LOG_FILE = "app.log"
 
 
class LogRedirector:
 
    def __init__(self, log_path: str):
        self.log_path = log_path
        self._original_stdout = None
        self._file = None
 
    def __enter__(self):
        # --- UZUPEŁNIJ ---
        pass
 
    def __exit__(self, exc_type, exc_val, exc_tb):
        # --- UZUPEŁNIJ ---
        pass
 
 
# Test
# --- UZUPEŁNIJ: użyj LogRedirector w bloku with ---