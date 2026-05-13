# Teorifrågor – ANSWERS.md

---

## 1. Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?

**Enhetstest** testar en enskild enhet – vanligtvis en funktion eller metod – i isolation. Externa beroenden ersätts ofta med mockar eller stubs. Målet är att verifiera att en liten, avgränsad del av koden fungerar korrekt.

**Integrationstest** testar hur flera enheter fungerar tillsammans. Istället för att isolera varje del låter man dem samspela och kontrollerar att gränssnitten mellan dem fungerar som förväntat. I det här projektet testas till exempel hur `BookStore` och `FavoriteBooks` samverkar.

**Regressionstest** används för att säkerställa att ny kod inte oavsiktligt förstör befintlig funktionalitet. Efter en ändring körs tidigare tester igen för att kontrollera att systemet fortfarande fungerar som tidigare. CI-pipelines används ofta för att köra regressionstester automatiskt vid varje push.

**Prestandatest** mäter systemets beteende under belastning, till exempel svarstider, genomströmning och stabilitet. Fokus ligger inte på korrekt funktionalitet utan på hastighet och skalbarhet. Exempel är lasttester och stresstester.

---

## 2. Beskriv hur det går till när man arbetar med TDD

TDD (Test-Driven Development) bygger på en iterativ utvecklingscykel i tre steg:

1. **Röd** – skriv ett test för funktionalitet som ännu inte finns. Testet ska misslyckas.
2. **Grön** – skriv den minimala kod som krävs för att testet ska bli godkänt.
3. **Refaktorera** – förbättra och städa upp koden utan att ändra beteendet. Testerna ska fortfarande vara gröna.

Cykeln upprepas för varje ny funktionalitet. Eftersom testerna skrivs före implementationen tvingas utvecklaren tänka igenom design och beteende innan koden skrivs. Det leder ofta till tydligare gränssnitt och mer testbar kod.

I det här projektet skrevs testerna i `test_laslist.py` innan implementationen i `laslist.py` skapades. Initialt misslyckades testerna eftersom modulen ännu inte existerade, varefter implementationen utvecklades stegvis tills testerna blev gröna.

---

## 3. Beskriv hur BDD skiljer sig från TDD

TDD är främst ett utvecklarfokuserat arbetssätt där fokus ligger på kodens design och korrekthet. Testerna är tekniska och riktar sig mot metoder, funktioner och returvärden.

BDD (Behaviour-Driven Development) bygger vidare på samma grundidé men fokuserar istället på systemets beteende ur användarens perspektiv. Testerna skrivs i ett naturligt språk med hjälp av Gherkin-syntaxen *Given / When / Then*, vilket gör dem läsbara även för personer utan programmeringskunskaper.

| Aspekt | TDD | BDD |
|---|---|---|
| Fokus | Kodenhet och design | Beteende och affärsvärde |
| Språk | Kod | Gherkin |
| Målgrupp | Utvecklare | Hela teamet |
| Abstraktionsnivå | Låg | Hög |
| Verktyg | unittest, pytest | Behave, Cucumber |

TDD och BDD ersätter inte varandra utan kompletterar varandra. BDD beskriver vad systemet ska göra ur användarens perspektiv, medan TDD säkerställer att implementationen fungerar korrekt på låg nivå.

---

## 4. Vilka sorters tester skulle du använda för en webbsida som Läslistan?

Om jag fick välja fritt skulle jag använda flera olika testnivåer för att täcka både backend och frontend.

**Enhetstester** skulle användas för backendlogik, exempelvis validering, affärslogik och hjälpfunktioner. De är snabba att köra och ger snabb feedback under utvecklingen.

**Integrationstester** skulle användas för att verifiera att olika delar av systemet fungerar tillsammans, exempelvis backend-klasser, API:er eller databaskopplingar.

**BDD- och end-to-end-tester** med Playwright skulle användas för frontend och användarflöden. Eftersom Läslistan är en SPA-applikation med navigering och tillståndshantering är det viktigt att testa systemet i en riktig browsermiljö.

Jag skulle även överväga **visuella tester** eller snapshots för att upptäcka oavsiktliga förändringar i användargränssnittet.

Däremot skulle jag inte prioritera avancerade prestandatester i ett tidigt skede eftersom applikationen är relativt liten och saknar höga belastningskrav.

För att automatisera regressionstester skulle jag använda **GitHub Actions** eller liknande CI-verktyg för att köra alla tester automatiskt vid varje push eller pull request.