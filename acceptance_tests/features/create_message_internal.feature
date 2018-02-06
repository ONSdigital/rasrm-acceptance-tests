Feature: Internal user to send message
  As an internal ONS user
  I need to be able to send a secure message
  So that I can query data that has been received

  Background: User already logged in
    Given The internal user is already signed in

  Scenario: 'To' field will be pre-populated with respondent name (up to 100 characters)
    When They choose to send them a secure message and navigated to the 'send message' page
    Then The 'To' field is populated with the respondent's name

  Scenario: User is able to enter free text in the subject field up to and including 100 characters
    Given The user is on the send message page
    When They enter text in the subject of the message
    Then They are able to enter free text up to and including 100 characters

  Scenario: User is able to enter free text  in the body of the message up to and including 10,000 characters
    Given The user is on the send message page
    When They enter text in the body of the message
    Then They are able to enter free text up to and including 10,000 characters

  Scenario: User is only able to send a message if there is text in the body of all fields ('Subject' and 'Message')
    Given The user is on the send message page
    When They enter text in the subject and body of the message
    Then They are able to send the message

  Scenario: The user is to be able to cancel out of sending a message (and navigated back to where they came from)
    Given The user is on the send message page
    When They choose to cancel out of sending a message
    Then They are navigated back to the page in which they navigated from

  Scenario: On sending the message the user is to be navigated to the inbox
    Given The user has entered text in the subject and body of the message
    When They select send
    Then They are navigated to the inbox of messages

  Scenario: On sending the message the user is to receive confirmation that the message has been sent
    Given The user has sent a secure message
    When They are navigated to the inbox of messages
    Then They are presented with confirmation that the message has been sent