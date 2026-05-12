# Läslistan – Testprojekt

Testprojekt för kursen TAP-HT25. Testar webbsidan [Läslistan](https://tap-ht25-testverktyg.github.io/exam/) med Python, Playwright och BDD (Behave + Gherkin).

---

## Vad har testats

### Backend (Python / unittest)
- **`BookStore.addBook`** – lägga till böcker, unika id:n, returnvärde
- **`BookStore.toggleFavorite`** – toggla favorit av/på, felhantering vid okänt id
- **`FavoriteBooks.add`** – lägga till favorit, duplikatskydd, flagga sätts
- **`FavoriteBooks.remove`** – ta bort favorit, flagga rensas, felhantering
- **Integrationstester** – klasserna används tillsammans i realistiska flöden

### Frontend (Playwright + Behave / BDD)
- **Katalog** – se böcker, navigering, favoritmarkering, lista uppdateras
- **Lägg till bok** – formulär, validering, ny bok visas i katalog
- **Mina böcker** – favoriter listas, ta bort favorit, tom lista
- **Statistik** – räknare för totalt antal böcker och antal favoriter
- **Navigering** – länkar mellan alla vyer fungerar

---

## Mappstruktur

```
laslist-projekt/
├── backend/
│   ├── laslist.py          # Implementationen (Book, BookStore, FavoriteBooks)
│   └── tests/
│       └── test_laslist.py # Enhetstester + integrationstester
├── features/
│   ├── katalog.feature
│   ├── lagg_till_bok.feature
│   ├── mina_bocker.feature
│   ├── statistik.feature
│   ├── navigering.feature
│   └── steps/
│       ├── common_steps.py
│       ├── katalog_steps.py
│       ├── lagg_till_bok_steps.py
│       ├── mina_bocker_steps.py
│       └── statistik_steps.py
├── pages/
│   ├── base_page.py
│   ├── katalog_page.py
│   ├── lagg_till_bok_page.py
│   ├── mina_bocker_page.py
│   └── statistik_page.py
├── environment.py          # Behave hooks (browser setup/teardown)
├── behave.ini
├── ANSWERS.md
├── STORIES.md
└── README.md
```

---

## Förutsättningar

- Python 3.10+
- Node.js (för Playwright-browsers)

---

## Installation

```bash
# Klona projektet
git clone https://github.com/henrikcederqvist/laslist-projekt.git
cd laslist-projekt

# Skapa och aktivera virtuell miljö
python3 -m venv venv
source venv/bin/activate        # Mac/Linux
# venv\Scripts\activate          # Windows

# Installera Python-beroenden
pip install behave playwright

# Installera Playwright-browsers
playwright install chromium
```

---

## Köra tester

### Backend (unittest)
```bash
python3 -m unittest backend/tests/test_laslist.py -v
```

### Frontend (Behave / BDD) – med synlig browser
```bash
behave
```

### Frontend – headless (för CI)
```bash
HEADLESS=true behave
```

### Specifik feature
```bash
behave features/katalog.feature
```

---

## CI

GitHub Actions kör automatiskt alla tester (headless) vid push till `main`.  
Se `.github/workflows/tests.yml`.
