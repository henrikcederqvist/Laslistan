# Läslistan – Testprojekt

Testprojekt för kursen TAP-HT25.  
Projektet testar webbsidan [Läslistan](https://tap-ht25-testverktyg.github.io/exam/) med Python, Playwright och BDD (Behave + Gherkin).

---

## Vad har testats

### Backend (Python / pytest)

#### Enhetstester
- `BookStore.addBook`
  - lägga till böcker
  - unika id:n
  - korrekt returnvärde

- `BookStore.toggleFavorite`
  - favoritmarkering av/på
  - felhantering vid okänt id

- `FavoriteBooks.add`
  - lägga till favorit
  - skydd mot dubletter
  - favoritflagga sätts korrekt

- `FavoriteBooks.remove`
  - ta bort favorit
  - favoritflagga rensas
  - felhantering

#### Integrationstester
- samspel mellan `BookStore` och `FavoriteBooks`
- realistiska användarflöden för favoriter

#### TDD-arbetssätt

Backenddelen har utvecklats med TDD enligt röd–grön–refaktorera:

1. Först skrevs tester för förväntat beteende i `backend/tests/test_laslist.py`.
2. Därefter implementerades minsta möjliga kod i `backend/laslist.py` för att testerna skulle bli gröna.
3. Slutligen refaktorerades koden utan att ändra beteendet, medan testerna fortsatte vara gröna.

Testerna fungerar därför både som verifiering och dokumentation av hur `BookStore` och `FavoriteBooks` ska bete sig.

---

### Frontend (Playwright + Behave / BDD)

#### Katalog
- visa böcker i katalogen
- visa titel och författare
- favoritmarkera böcker
- ta bort favoritmarkering
- flera favoriter fungerar oberoende av varandra

#### Lägg till bok
- formulär för titel och författare
- lägga till bok
- validering av tomma fält
- formulär töms efter inskickning
- ny bok visas direkt i katalogen

#### Mina böcker
- favoritböcker visas i lista
- tom favoritlista visas korrekt
- ta bort favorit direkt från Mina böcker
- korrekt antal favoriter visas

#### Statistik
- totalt antal böcker visas
- antal favoritmarkerade böcker visas
- statistik uppdateras vid ändringar

#### Navigering
- navigering mellan alla vyer fungerar
- menylänkar leder till rätt sida

---

## Tekniker och verktyg

- Python
- pytest
- Behave
- Gherkin
- Playwright
- GitHub Actions (CI)

---

## Designmönster

Projektet använder Page Object Pattern för att återanvända frontendlogik och minska duplicerad kod i step-filerna.

---

## Mappstruktur

```text
laslist-projekt/
├── backend/
│   ├── laslist.py
│   └── tests/
│       └── test_laslist.py
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
├── environment.py
├── behave.ini
├── requirements.txt
├── ANSWERS.md
├── STORIES.md
└── README.md
```

---

## Installation

```bash
git clone https://github.com/henrikcederqvist/laslist-projekt.git

cd laslist-projekt

python -m venv .venv
```

### Aktivera virtuell miljö

#### Windows

```bash
.venv\Scripts\activate
```

#### Mac/Linux

```bash
source .venv/bin/activate
```

### Installera beroenden

```bash
pip install -r requirements.txt
```

### Installera Playwright-browser

```bash
playwright install chromium
```

---

## Köra tester

### Backendtester

```bash
pytest backend/tests -v
```

### Frontendtester

```bash
behave
```

### Frontendtester med synlig browser

#### Windows PowerShell

```bash
$env:HEADLESS="false"
behave
```

#### Mac/Linux

```bash
HEADLESS=false behave
```

### Frontendtester headless (CI-läge)

#### Windows PowerShell

```bash
$env:HEADLESS="true"
behave
```

#### Mac/Linux

```bash
HEADLESS=true behave
```

---

## CI

Projektet använder GitHub Actions för Continuous Integration.

Alla tester körs automatiskt vid:
- push till `main`
- pull requests mot `main`

CI kör:
- flake8
- pytest
- Behave + Playwright (headless)