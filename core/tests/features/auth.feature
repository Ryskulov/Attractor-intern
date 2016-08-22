Feature: Authorization

  Scenario: Registration
    Open "registration" page
    Fill "username" with "myusername"
    Fill "email" with "user@example.com"
    Fill "password" with "1234"
    Fill "last_name" with "Chingiz
    Click "signup button"

#  Scenario: Authorization
#    Open "authorization" page
#    Fill "username" with "myusername"
#    Fill "password" with "1234"
#    Click "login button"
#    See "Hello! Again..." in "status message"
