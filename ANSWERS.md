# Teorifrågor – ANSWERS.md

---

## 1. Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?

**Enhetstest** testar en enskild enhet – typiskt en funktion eller metod – i isolation. Externa beroenden ersätts med mockar eller stubs. Målet är att verifiera att en liten, avgränsad del av koden gör precis vad den ska, och ingenting annat.

**Integrationstest** testar hur flera enheter fungerar *tillsammans*. Istället för att isolera varje del låter man dem samspela och kontrollerar att gränssnitten stämmer. I det här projektet testas till exempel hur `BookStore` och `FavoriteBooks` samverkar: en bok läggs till i store, toggles och läggs sedan till i favoriter.

**Regressionstest** syftar till att säkerställa att ny kod inte oavsiktligt förstör befintlig funktionalitet. Det är inte en separat testtyp tekniskt sett – man återkör befintliga enhetstester och integrationstester efter en ändring. Om något som fungerade tidigare nu misslyckas har en regression uppstått. CI-pipelines används ofta för att köra regressionstester automatiskt vid varje push.

**Prestandatest** mäter systemets beteende under belastning: svarstider, genomströmning och stabilitet. Det handlar inte om korrekthet utan om hastighet och skalbarhet. Exempel är lasttest (många simultana användare) och stresstester (ta systemet till bristningsgränsen).

---

## 2. Beskriv hur det går till när man arbetar med TDD

TDD (Test-Driven Development) bygger på en kort, upprepad cykel i tre steg:

1. **Röd** – Skriv ett test för funktionalitet som *inte finns än*. Testet ska misslyckas.
2. **Grön** – Skriv den minimala kod som krävs för att testet ska bli grönt. Inget mer.
3. **Refaktorera** – Städa upp koden utan att ändra beteendet. Testerna ska fortfarande vara gröna.

Cykeln upprepas för varje ny bit funktionalitet. Eftersom testerna skrivs före koden tvingas man tänka igenom gränssnittet och beteendet innan man börjar implementera. Det leder till väldefinierade funktioner med tydligt syfte och en testsvit som växter organiskt med koden.

I det här projektet skrevs `test_laslist.py` i sin helhet *innan* `laslist.py` skapades. Alla tester kraschade med `ModuleNotFoundError` (röd fas), varefter implementationen skrevs för att göra dem gröna.

---

## 3. Beskriv hur BDD skiljer sig från TDD

TDD är ett **utvecklarverktyg** – fokus ligger på kodens design och korrekthet, och testerna är tekniska (metoder, returvärden, undantag).

BDD (Behaviour-Driven Development) är en **kommunikationsmetod** som bygger vidare på TDD:s cykel men lyfter blicken till affärsbeteende och användarbehov. Testerna skrivs i ett naturligt språk (Gherkin: *Given / When / Then*) som är läsbart för alla – inte bara utvecklare.

Några viktiga skillnader:

| Aspekt | TDD | BDD |
|---|---|---|
| Fokus | Kodenhet, design | Beteende, affärsvärde |
| Språk | Kod (Python, JS…) | Gherkin (Given/When/Then) |
| Målgrupp | Utvecklare | Hela teamet, inkl. produktägare |
| Abstraktionsnivå | Låg (metod/klass) | Hög (funktion/flöde) |
| Verktyg | unittest, pytest, Jest | Behave, Cucumber, SpecFlow |

I praktiken ersätter inte BDD TDD – de kompletterar varandra. BDD-scenarierna beskriver vad systemet ska göra ur användarens perspektiv, medan enhetstester (TDD) säkerställer att varje del av implementationen är korrekt.

---

## 4. Vilka sorters tester skulle du använda för en webbsida som Läslistan?

Om jag fick välja förutsättningslöst skulle jag använda en kombination av fyra testnivåer:

**Enhetstester (pytest)** för all affärslogik på backend: klasser, valideringslogik och datamappning. De är snabba, isolerade och ger snabb feedback under utveckling.

**Integrationstester** för att verifiera att backend-klasserna samverkar korrekt – precis som i den här uppgiften. Om projektet hade en databas eller ett API skulle integrationstesterna täcka det gränssnittet.

**BDD-tester med Playwright** för frontend och end-to-end-flöden. Gherkin-scenarierna dokumenterar funktionaliteten på ett sätt som även icke-tekniska intressenter förstår, och Playwright kör testerna i en riktig browser. Det är särskilt värdefullt för Läslistan eftersom sidan är en React-SPA med navigering och tillståndshantering som behöver testas som ett helhetssystem.

**Snapshot-/visuella tester** (t.ex. Playwright screenshots) skulle jag överväga för att fånga oavsiktliga UI-förändringar, men det är lägre prioritet.

Jag skulle *inte* investera i prestandatester i dagsläget – webbsidan är statisk och har inga skalbarhetskrav. Däremot skulle jag sätta upp **CI med GitHub Actions** som kör alla tester headless vid varje push, för att fånga regressioner tidigt.
