Feature: Lägg till bok

  Background:
    Given att jag befinner mig på sidan för att lägga till bok

  Scenario: Formuläret har fält för titel och författare
    Then ska jag se ett fält för boktitel
    And ska jag se ett fält för författare

  Scenario: Lägga till en bok med giltig data
    When jag fyller i titeln "Exjobbet" och författaren "Anna Svensson"
    And jag skickar in formuläret
    And jag navigerar till katalogsidan
    Then ska boken "Exjobbet" finnas i listan

  Scenario: Formuläret tömmer sig efter inskickning
    When jag fyller i titeln "Rensningstest" och författaren "Bok Boksson"
    And jag skickar in formuläret
    Then ska formulärfälten vara tomma

  Scenario Outline: Validering – formuläret avvisas om fält saknas
    When jag fyller i titeln "<titel>" och författaren "<författare>"
    And jag försöker skicka in formuläret
    Then ska formuläret inte ha skickats in

    Examples:
      | titel     | författare |
      |           | Svensson   |
      | En titel  |            |
      |           |            |