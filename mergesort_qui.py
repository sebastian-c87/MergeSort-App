import tkinter as tk
from tkinter import messagebox

# Licznik kroków (rekurencji) - ile razy algorytm wykonał scalanie
merge_steps = 0

# Historia działania algorytmu (lista kroków scalania do pokazania użytkownikowi)
history = []

def merge_sort(arr, depth=0):
    """
    Funkcja sortująca listę liczb metodą sortowania przez scalanie (merge sort).
    Działa rekurencyjnie dzieląc listę na pół, sortując części i scalając je w całość.
    """
    global merge_steps
    if len(arr) <= 1:
        # Jeśli lista zawiera 1 lub 0 elementów, jest już posortowana
        return arr

    # Znalezienie środka listy, podział na dwie części
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], depth + 1)  # Rekurencyjne sortowanie lewej połowy
    right = merge_sort(arr[mid:], depth + 1)  # Rekurencyjne sortowanie prawej połowy

    merge_steps += 1  # Zliczamy wykonane scalanie
    merged = merge(left, right)  # Scal dwie posortowane listy w jedną

    # Dodanie szczegółowego opisu scalania do historii
    indent = '    ' * depth  # Wcięcie zależne od głębokości rekurencji
    history.append(f"{indent}Scalanie: {left} + {right} -> {merged}")

    return merged

def merge(left, right):
    """
    Funkcja pomocnicza do łączenia dwóch posortowanych list w jedną.
    Elementy są porównywane i dodawane do wyniku w odpowiedniej kolejności.
    """
    result = []
    i = j = 0

    # Porównujemy elementy z obu list i dodajemy mniejszy z nich do wyniku
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Dodajemy pozostałe elementy z lewej i prawej listy (jeśli jakieś zostały)
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def sort_numbers():
    """
    Funkcja wywoływana po kliknięciu przycisku 'Sortuj'.
    Przetwarza dane wejściowe, wykonuje sortowanie i aktualizuje interfejs.
    """
    global merge_steps, history
    input_data = entry.get()  # Pobranie danych z pola tekstowego

    try:
        # Konwersja tekstu na listę liczb całkowitych
        numbers = list(map(int, input_data.split(',')))
    except ValueError:
        # Obsługa błędu: jeśli użytkownik wpisał coś innego niż liczby
        messagebox.showerror("Błąd", "Wprowadź liczby oddzielone przecinkami (np. 5,3,8,1)")
        return

    # Resetowanie liczników i historii
    merge_steps = 0
    history = []
    sorted_list = merge_sort(numbers)  # Uruchomienie sortowania

    # Wyświetlenie wyniku sortowania i liczby kroków
    result_label.config(text=f"Posortowana lista: {sorted_list}\nLiczba kroków: {merge_steps}")

    # Wyświetlenie historii działania algorytmu
    history_text.delete("1.0", tk.END)
    history_text.insert(tk.END, "Historia działania algorytmu:\n\n")
    for step in history:
        history_text.insert(tk.END, step + "\n")

# Utworzenie głównego okna aplikacji
root = tk.Tk()
root.title("Merge Sort - Edukacyjna aplikacja")
root.geometry("600x500+100+100")  # Rozmiar i pozycja startowa okna (w lewym górnym rogu ekranu)

# Etykieta z instrukcją
info_label = tk.Label(root, text="Wprowadź liczby oddzielone przecinkami (np. 4,1,6,2)", font=("Arial", 10))
info_label.pack(pady=10)

# Pole tekstowe do wprowadzania danych
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Przycisk uruchamiający sortowanie
sort_button = tk.Button(root, text="Sortuj", command=sort_numbers)
sort_button.pack(pady=10)

# Etykieta z wynikiem sortowania
result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=10)

# Ramka na historię działania algorytmu
history_frame = tk.Frame(root)
history_frame.pack(pady=5)

# Nagłówek historii
history_label = tk.Label(history_frame, text="Historia działania algorytmu:", font=("Arial", 10, "bold"))
history_label.pack()

# Pole tekstowe do wyświetlania historii działania
history_text = tk.Text(history_frame, height=15, width=70)
history_text.pack()

# Uruchomienie pętli głównej aplikacji GUI
tk.mainloop()
