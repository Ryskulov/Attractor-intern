Feature: Authorization

  Scenario: Registration
    Open "registration" page
    Fill "username" with "myusername"
    Fill "email" with "user@example.com"
    Fill "password" with "1234"
    Fill "first_name" with "Chingiz"
    Click "signup_button"

  Scenario: Authorization
    Open "authorization" page
    Fill "username" with "myusername"
    Fill "password" with "1234"
    Click "login_button"

