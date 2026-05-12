# US-NAV-1
Feature: Navigering
  Som användare vill jag kunna navigera mellan alla vyer
  så att jag alltid hittar rätt sida.

  Scenario: Startsidan är katalogen
    Given att jag öppnar webbsidan
    Then ska jag befinna mig på katalogsidan

  Scenario: Navigera till Lägg till bok
    Given att jag befinner mig på katalogsidan
    When jag klickar på länken "Lägg till bok"
    Then ska jag befinna mig på sidan för att lägga till bok

  Scenario: Navigera till Mina böcker
    Given att jag befinner mig på katalogsidan
    When jag klickar på länken "Mina böcker"
    Then ska jag befinna mig på sidan för mina böcker

  Scenario: Navigera till Statistik
    Given att jag befinner mig på katalogsidan
    When jag klickar på länken "Statistik"
    Then ska jag befinna mig på statistiksidan

  Scenario: Navigera tillbaka till Katalog från annan vy
    Given att jag befinner mig på statistiksidan
    When jag klickar på länken "Katalog"
    Then ska jag befinna mig på katalogsidan

  Scenario Outline: Alla menylänkar leder till rätt vy
    Given att jag befinner mig på katalogsidan
    When jag klickar på länken "<lank>"
    Then ska sidtiteln innehålla "<titel>"

    Examples:
      | lank           | titel          |
      | Katalog        | Katalog        |
      | Lägg till bok  | Lägg till bok  |
      | Mina böcker    | Mina böcker    |
      | Statistik      | Statistik      |
