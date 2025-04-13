# 🧠 Merge Sort – Educational Sorting App

A lightweight web app built with **Python** and **Flask**, designed to visually demonstrate the **Merge Sort** algorithm step-by-step. The application shows how lists are split and merged recursively, giving insight into the internal mechanics of the sorting process.

## ✨ Features

- 🔢 Enter any sequence of numbers (e.g. `5,3,1,8`)
- 🧠 Watch how the algorithm recursively divides and merges
- 📈 Track number of **merge operations**
- ✅ Visual representation of every **merge step**
- 🌐 Runs in the browser, no installation needed
- 📦 Comes with `.exe` file – **no Python required**

## 🚀 Quick Start

1. ✅ Clone or download this repository.
2. 🐍 Make sure Python & Flask are installed.
3. ▶️ Run `app_mergesort.py`:
   ```bash
   python app_mergesort.py
   ```
4. 🌐 The app will auto-launch in your browser at `http://127.0.0.1:5000`.

## 📦 Compiled EXE Version

The app is compiled to `.exe` using:
```bash
pyinstaller --onefile --windowed --icon=ikona.ico app_mergesort.py
```

✅ After launching the `.exe`:
- A terminal window opens (optional),
- The browser opens automatically.

## ⚠️ SmartScreen Warning

On Windows, you might see:
> ❗ Windows protected your PC

This is a standard **SmartScreen warning**.

Click:
1. `More info`
2. `Run anyway`

🟢 This application is safe and open-source – it’s not digitally signed.

## 📘 Algorithm Explanation

**Merge Sort** follows the *Divide and Conquer* principle:

1. Divide the list in half.
2. Recursively sort both halves.
3. Merge both halves into a sorted list:
   - Compare elements from both halves.
   - Append smaller one to result list `e`.
4. Each step (adding element to `e`) is counted as one **merge operation**.

⏱️ Time complexity:
- Average/Worst: **O(n log n)**
- Space: **O(n)**

## 📁 Releases

The compiled `.exe` will be available here:
👉 [GitHub Releases](https://github.com/YourUsername/RepoName/releases) *(update after publishing)*

## 📜 License

This project is open for everyone.  
Created by **Sebastian Ciborowski** – student at Vistula University, Warsaw.  
Feedback and contributions are welcome.  
**For educational use only.**

---

# 🇵🇱 Merge Sort – Edukacyjna aplikacja do sortowania

Aplikacja webowa napisana w **Pythonie** z użyciem **Flask**, która krok po kroku prezentuje działanie klasycznego algorytmu **Merge Sort (sortowanie przez scalanie)**.

## ✨ Funkcje

- 🔢 Wpisz dowolny ciąg liczb (np. `5,3,1,8`)
- 🧠 Obserwuj rekurencyjne dzielenie i scalanie list
- 📈 Zliczanie liczby **operacji scalania**
- ✅ Historia każdego kroku z listami `a`, `b`, `e`
- 🌐 Działa w przeglądarce – bez instalacji
- 📦 Gotowy plik `.exe` – **nie wymaga Pythona**

## 🚀 Jak uruchomić

1. ✅ Pobierz lub sklonuj repozytorium.
2. 🐍 Upewnij się, że masz zainstalowany Python i Flask.
3. ▶️ Uruchom `app_mergesort.py`:
   ```bash
   python app_mergesort.py
   ```
4. 🌐 Aplikacja sama otworzy się w przeglądarce: `http://127.0.0.1:5000`

## 📦 Wersja EXE

Utworzono przy pomocy:
```bash
pyinstaller --onefile --windowed --icon=ikona.ico app_mergesort.py
```

✅ Po uruchomieniu `.exe`:
- otwiera się terminal (opcjonalnie),
- aplikacja startuje automatycznie w przeglądarce.

## ⚠️ Ostrzeżenie SmartScreen

Może pojawić się komunikat:
> ❗ System Windows ochronił ten komputer

To standardowy komunikat Microsoft SmartScreen.

Kliknij:
1. `Więcej informacji`
2. `Uruchom mimo to`

🟢 Aplikacja jest bezpieczna, lecz nie posiada podpisu cyfrowego.

## 📘 Jak działa algorytm Merge Sort

1. Lista wejściowa jest dzielona na pół.
2. Każda część sortowana rekurencyjnie.
3. Następnie scala się je w jedną posortowaną listę:
   - Porównuje pierwszy element z każdej listy,
   - Dodaje mniejszy do listy wynikowej `e`.
4. Każde dodanie do `e` to **jeden krok sortowania**.

⏱️ Złożoność czasowa:
- Średnia / najgorszy przypadek: **O(n log n)**
- Pamięciowa: **O(n)**

## 📁 Release

Gotowy plik `.exe` będzie dostępny tutaj:  
👉 [Releases na GitHubie](https://github.com/YourUsername/RepoName/releases) *(link do uzupełnienia)*

## 📜 Licencja

Projekt open-source dostępny dla wszystkich.  
Autor: **Sebastian Ciborowski**, student Akademii Finansów i Biznesu Vistula w Warszawie.  
Zachęcam do komentowania i udostępniania.  
**Do użytku edukacyjnego.**

