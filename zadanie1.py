#
# Poniższy fragment kodu pochodzi z prostej aplikacji do
# zarządzania kontami użytkowników. Zawiera kilka potencjalnie
# niebezpiecznych operacji: odczyt pliku konfiguracyjnego,
# parsowanie JSON oraz logowanie zdarzenia
#
# Polecenie:
# Opakuj funkcje "load_user_config" w try/except/finally oraz obsłuż wyrzucone 
# wyjątki (FileNotFoundError oraz json.JSONdecodeError) zakańczając proces printem
# "Zakończenie wczytywania niezależnie od wyniku"
#
 
import json
import os
 
CONFIG_PATH = "user_config.json"
 
 
def load_user_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
 
 
def initialize_app():
    config = None
 
    # --- UZUPEŁNIJ PONIŻEJ ---
 
    config = load_user_config(CONFIG_PATH)   # ta linia ma pozostać wewnątrz try
 
    # --- KONIEC UZUPEŁNIENIA ---
 
    if config:
        print(f"Załadowano konfigurację: {config}")
 
 
# TESTOWANIE
print("=== Test: brak pliku ===")
initialize_app()
 
print("\n=== Test: poprawny plik ===")
with open(CONFIG_PATH, "w", encoding="utf-8") as f:
    json.dump({"theme": "dark", "language": "pl"}, f)
initialize_app()
os.remove(CONFIG_PATH)
 
print("\n=== Test: zepsuty JSON ===")
with open(CONFIG_PATH, "w", encoding="utf-8") as f:
    f.write("{ to nie jest json }")
initialize_app()
os.remove(CONFIG_PATH)