Feature: Decorator
  Scenario: Creating an empty window
    Given an empty window
    When the window works flawlessly
    Then get the result Empty Window

  Scenario: Adding a border to a window
    Given an empty window
    And the border is given
    When performing work at the border
    Then get the result <Border>Empty Window</Border>

  Scenario: Adding a property-thick to border around the window.
    Given an empty window
    And the border is given
    And a thick is given
    When wonderful work in a thick border
    Then get the result <Thick><Border>Empty Window</Border></Thick>