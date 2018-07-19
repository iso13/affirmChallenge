Feature: Loans
  As an Affirm banker
  I need to borrow money from banking partners
  So I can extend the loans to customers

  Scenario: Develop loans
    Given I follow the covenants of banned_state and max_default_likelihood
    When I figure the expected yield from each loan
    Then I should see a loan assignment for each facility
    And I should see an expected yield of each facility

