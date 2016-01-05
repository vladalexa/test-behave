Feature: Login BL

  Scenario: Log into BL
    Given I am on BL log in page
    When I log in
    Then I see the welcome page