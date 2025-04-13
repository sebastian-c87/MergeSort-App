# Importujemy niezbędne funkcje z biblioteki Flask
from flask import Flask, request, render_template_string

import webbrowser
import threading


# Inicjalizujemy aplikację Flask
app = Flask(__name__)

# HTML do wyświetlenia formularza i wyników – używamy render_template_string
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Merge Sort – Edukacyjna aplikacja</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        .green { color: green; font-weight: bold; }
        .blue { color: blue; font-weight: bold; }
        .step { margin-top: 10px; white-space: pre-wrap; }
        textarea { width: 100%; height: 200px; }
    </style>
</head>
<body>
    <h2>🔢 Merge Sort – Sortowanie przez scalanie</h2>
    <form method="POST">
        <label>Wprowadź liczby oddzielone przecinkami:</label><br>
        <input type="text" name="numbers" value="{{ request.form.get('numbers', '') }}" size="50">
        <button type="submit">Sortuj</button>
    </form>
    {% if wynik %}
        <p class="green">✅ Lista przed sortowaniem: {{ wejsciowa }}</p>
        <p class="green">✅ Posortowana lista: {{ wynik }}</p>
        <p class="blue">📘 Liczba kroków (pełnych operacji scalania): {{ kroki }}</p>
        <h4>🧠 Szczegółowa historia działania algorytmu:</h4>
        <textarea readonly>{{ historia }}</textarea>
    {% endif %}
</body>
</html>
"""

# Zmienna globalna do zapisywania historii działania algorytmu
history = []

# Licznik kroków – ile razy wykonano scalanie
merge_steps = 0

# Funkcja główna – merge_sort
def merge_sort(arr):
    """
    Sortuje rekurencyjnie listę liczb za pomocą algorytmu Merge Sort.
    """
    global merge_steps, history

    # Jeśli lista ma 0 lub 1 element, jest już posortowana
    if len(arr) <= 1:
        return arr

    # Dzielimy listę na dwie części
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # Rekurencyjnie sortujemy lewą część
    right = merge_sort(arr[mid:])  # Rekurencyjnie sortujemy prawą część
    
    # Scalanie posortowanych części
    merged = merge(left, right)

    # Zapisujemy historię scalania
    merge_steps += 1
    history.append(f"Krok {merge_steps}:\n  a = {left}\n  b = {right}\n  wynik = {merged}\n")
    
    return merged

# Funkcja pomocnicza merge – łączy dwie posortowane listy w jedną
def merge(left, right):
    """
    Scala dwie posortowane listy w jedną, porównując po kolei elementy.
    """
    result = []  # Lista wynikowa
    i = j = 0    # Indeksy dla lewej (i) i prawej (j) listy

    # Porównujemy elementy z obu list i dodajemy mniejszy do wynikowej
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Dodajemy pozostałe elementy z lewej listy (jeśli zostały)
    result.extend(left[i:])
    
    # Dodajemy pozostałe elementy z prawej listy (jeśli zostały)
    result.extend(right[j:])
    
    return result


# Dekorator Flask @app.route służy do przypisania konkretnej funkcji do określonego adresu URL (tutaj "/")
# Oznacza to, że kiedy użytkownik wejdzie na stronę główną (np. http://localhost:5000/), wywoła się funkcja `index()`
# `methods=['GET', 'POST']` oznacza, że obsługujemy dwa typy żądań HTTP:
# - GET: domyślne żądanie (np. kiedy użytkownik po prostu otwiera stronę)
# - POST: żądanie przesłania formularza (np. po kliknięciu "Sortuj" z wpisanymi liczbami)
# Dzięki temu możemy rozróżniać, czy strona ma tylko się wyświetlić (GET), czy przetworzyć dane wejściowe (POST)

# Główna funkcja strony głównej (route "/")
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Obsługuje żądania GET i POST. Po przesłaniu formularza wykonuje sortowanie
    i zwraca wynik z historią oraz liczbą kroków.
    """
    global merge_steps, history

    wynik = None        # Zmienna na wynik sortowania
    historia = ""       # Zmienna na historię kroków
    kroki = 0           # Licznik kroków
    wejsciowa = ""      # Oryginalna lista użytkownika (do pokazania)

    # Jeśli użytkownik wysłał formularz (POST)
    if request.method == 'POST':
        dane = request.form.get('numbers', '')  # Pobieramy liczby od użytkownika
        try:
            liczby = list(map(int, dane.split(',')))  # Konwertujemy na listę int
            wejsciowa = liczby.copy()  # Zapisujemy oryginalną listę
            merge_steps = 0            # Reset licznika kroków
            history = []               # Reset historii
            wynik = merge_sort(liczby)  # Wykonanie sortowania
            kroki = merge_steps         # Przypisanie liczby kroków
            historia = "\n".join(history)  # Połączenie historii w jeden string
        except ValueError:
            wynik = "❌ Błąd: Wprowadź tylko liczby oddzielone przecinkami!"  # Błąd danych wejściowych

    # Renderujemy gotowy HTML z danymi
    return render_template_string(
        HTML,
        wynik=wynik,
        historia=historia,
        kroki=kroki,
        wejsciowa=wejsciowa,
        request=request
    )

# Uruchomienie serwera aplikacji Flask
# Funkcja uruchamiająca serwer Flask
def run_app():
    # Rozpoczyna działanie lokalnego serwera (domyślnie na porcie 5000)
    app.run()

# Główna część programu – tylko uruchamiana, jeśli skrypt jest wykonywany bezpośrednio
if __name__ == '__main__':
    # Używamy osobnego wątku (Timer), aby po 1.25 sekundy automatycznie otworzyć przeglądarkę
    # Dzięki temu użytkownik nie musi ręcznie wchodzić na http://127.0.0.1:5000
    threading.Timer(1.25, lambda: webbrowser.open("http://127.0.0.1:5000")).start()
    
    # Uruchamiamy aplikację Flask
    run_app()