Feature: #Enter feature name here
  # Enter feature description here

  Scenario: Sign in successfully
    Given the user is in the login page
    When the user enters user name "Thach Hoang"
    And the user enters user password "Thach Hoang"
    And the user clicks Sign In button
    Then the profile name is displayed as "Thach Hoang Ngoc"
