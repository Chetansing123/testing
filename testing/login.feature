Feature: validate login
  scenario: verify login with correct login details
  Given When user in login page with correct username and password
  When user enter correct username and password
  And user click on submit button
  Then user redirect to home page and verify the title of the page