# US-ADD-1, US-ADD-2, US-ADD-3
Feature: Lägg till bok
  Som användare vill jag kunna lägga till nya böcker i katalogen
  så att jag kan utöka listan med titlar som saknas.

  Background:
    Given att jag befinner mig på sidan för att lägga till bok

  Scenario: Formuläret har fält för titel och författare
    Then ska jag se ett fält för boktitel
    And ska jag se ett fält för författare

  Scenario: Lägga till en bok med giltig data
    When jag fyller i titeln "Exjobbet" och författaren "Anna Svensson"
    And jag skickar in formuläret
    Then ska boken "Exjobbet" visas i katalogen

  Scenario: Ny bok syns i katalogen direkt
    When jag fyller i titeln "Ny testbok" och författaren "Test Testsson"
    And jag skickar in formuläret
    And jag navigerar till katalogsidan
    Then ska boken "Ny testbok" finnas i listan

  Scenario: Formuläret tömmer sig efter inskickning
    When jag fyller i titeln "Rensningstest" och författaren "Bok Boksson"
    And jag skickar in formuläret
    Then ska formulärfälten vara tomma

  Scenario Outline: Validering – formuläret avvisas om fält saknas
    When jag fyller i titeln "<titel>" och författaren "<forfattare>"
    And jag försöker skicka in formuläret
    Then ska formuläret inte ha skickats in

    Examples:
      | titel    | forfattare |
      |          | Svensson   |
      | En titel |            |
      |          |            |
