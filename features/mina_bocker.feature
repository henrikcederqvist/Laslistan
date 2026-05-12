# US-FAV-1, US-FAV-2, US-FAV-3
Feature: Mina böcker
  Som användare vill jag se och hantera mina favoritböcker
  så att jag snabbt hittar det jag vill läsa.

  Scenario: Tom lista visas när inga favoriter finns
    Given att inga böcker är markerade som favoriter
    When jag navigerar till Mina böcker
    Then ska jag se ett meddelande om att listan är tom

  Scenario: Favoritbok visas i Mina böcker
    Given att jag har markerat den första boken som favorit i katalogen
    When jag navigerar till Mina böcker
    Then ska den boken finnas i min lista

  Scenario: Flera favoriter visas alla
    Given att jag har markerat 3 böcker som favoriter i katalogen
    When jag navigerar till Mina böcker
    Then ska jag se 3 böcker i min lista

  Scenario: Ta bort en favorit från Mina böcker
    Given att jag har markerat den första boken som favorit i katalogen
    And jag befinner mig på Mina böcker
    When jag tar bort den första boken från mina favoriter
    Then ska boken inte längre finnas i min lista

  Scenario: Mina böcker är tom efter att sista favoriten tagits bort
    Given att jag har markerat den första boken som favorit i katalogen
    And jag befinner mig på Mina böcker
    When jag tar bort den första boken från mina favoriter
    Then ska jag se ett meddelande om att listan är tom

  Scenario Outline: Rätt antal favoriter visas
    Given att jag har markerat <antal> böcker som favoriter i katalogen
    When jag navigerar till Mina böcker
    Then ska jag se <antal> böcker i min lista

    Examples:
      | antal |
      | 1     |
      | 2     |
      | 3     |
