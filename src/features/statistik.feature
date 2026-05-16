# US-STAT-1, US-STAT-2, US-STAT-3
Feature: Statistik
  Som användare vill jag se statistik om katalogen och mina favoriter
  så att jag får en snabb överblick.

  Background:
    Given att jag befinner mig på statistiksidan

  Scenario: Statistiksidan visar totalt antal böcker
    Then ska jag se det totala antalet böcker

  Scenario: Statistiksidan visar antal favoriter
    Then ska jag se antalet favoritmarkerade böcker

  Scenario: Antalet favoriter är noll när inga böcker är markerade
    Given att inga böcker är markerade som favoriter
    When jag navigerar till statistiksidan
    Then ska antalet favoriter visas som 0

  Scenario: Statistiken uppdateras när en bok läggs till
    Given att jag noterar det aktuella totala antalet böcker
    When jag lägger till en ny bok via formuläret
    And jag navigerar till statistiksidan
    Then ska det totala antalet böcker ha ökat med 1

  Scenario: Statistiken uppdateras när en bok markeras som favorit
    Given att jag noterar det aktuella antalet favoriter
    When jag markerar en bok som favorit i katalogen
    And jag navigerar till statistiksidan
    Then ska antalet favoriter ha ökat med 1

  Scenario: Statistiken uppdateras när en favorit tas bort
    Given att en bok är markerad som favorit
    And jag noterar det aktuella antalet favoriter
    When jag tar bort favoritmarkeringen
    And jag navigerar till statistiksidan
    Then ska antalet favoriter ha minskat med 1

  Scenario Outline: Korrekt antal favoriter visas i statistik
    Given att jag har markerat <antal> böcker som favoriter i katalogen
    When jag navigerar till statistiksidan
    Then ska antalet favoriter visas som <antal>

    Examples:
      | antal |
      | 0     |
      | 1     |
      | 3     |