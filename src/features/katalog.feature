# US-KAT-1, US-KAT-2, US-KAT-3, US-KAT-4
Feature: Katalog
  Som användare vill jag se och hantera böcker i katalogen
  så att jag kan bläddra bland titlar och markera favoriter.

  Background:
    Given att jag befinner mig på katalogsidan

  Scenario: Katalogen visar böcker
    Then ska jag se minst en bok i listan

  Scenario: En bok har titel och författare
    Then ska varje bok ha en synlig titel
    And ska varje bok ha en synlig författare

  Scenario: Favoritmarkera en bok
    When jag klickar på favoritknappen för den första boken
    Then ska den första boken vara markerad som favorit

  Scenario: Ta bort favoritmarkering
    Given att den första boken är markerad som favorit
    When jag klickar på favoritknappen för den första boken igen
    Then ska den första boken inte längre vara markerad som favorit

  Scenario: Klicka favorit två gånger återgår till icke-favorit
    When jag klickar på favoritknappen för den första boken
    And jag klickar på favoritknappen för den första boken
    Then ska den första boken inte längre vara markerad som favorit

  Scenario Outline: Favoritmarkera flera böcker oberoende av varandra
    When jag favoritmarkerar bok nummer <nummer>
    Then ska bok nummer <nummer> vara markerad som favorit
    And ska övriga böcker inte vara påverkade

    Examples:
      | nummer |
      | 1      |
      | 2      |
      | 3      |