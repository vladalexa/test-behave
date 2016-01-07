Feature: Signup staging

  Scenario: Signup to the staging environment with alphanumerical credentials
    Given I am on the staging1D login page
    When I click on Signup element
    Then I can see the Signup page
    When I sign up with the credentials: xxx@mail.com, kjshf874365gf873
    Then I can see the Onboarding page
    When I click on Cancel element
