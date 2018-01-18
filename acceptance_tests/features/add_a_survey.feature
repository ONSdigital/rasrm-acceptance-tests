Feature: Add a survey
  As a Respondent
  I need to be able to enrol for a new survey with my existing account
  So that I can respond on behalf of a business

  Background: User already logged in
    Given the user is signed into their account
  
  @us334-addSurvey_s01
  Scenario: Enter the enrolment code
    When they add a new survey
    Then they are able to enter the enrolment code

  @us334-addSurvey_s02
  Scenario: View survey & organisation that they are enrolling for
    And selects to add a new survey
    When they enter a valid enrolment code
    Then they are to be notified

  @us334-addSurvey_s03
  Scenario: Invalid entry of an enrolment code
    And selects to add a new survey
    When they enter an invalid enrolment code
    Then they are to be notified

  @us334-addSurvey_s04, @enrolment, @smoke
  Scenario: View new survey in my surveys
    And the user has entered a valid enrolment code
    When they continue and confirm that the organisation and survey that they are enrolling for is correct
    Then the new survey is to be listed in My Surveys and confirmation is presented to the user

  @us334-addSurvey_s05
  Scenario: User can cancel at any point
    And the user has entered their enrolment code
    When they navigate to the confirm organisation page and click cancel
    Then the user is navigated back to their "To do" list and they have not enrolled for that survey