*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Register With Valid Username And Password
    Go To Register Page
    Set Username  hamidaebadi
    Set Password  hamid1234
    Set Confirmatin Password  hamid1234
    Submit Register
    Welcom Page Should Be Open

Register With Too Short Username And Valid Password
    Go To Register Page
    Set Username  h
    Set Password  hamid1234
    Set Confirmatin Password  hamid1234
    Submit Register
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Go To Register Page
    Set Username  hamidebadi
    Set Password  ab23
    Set Confirmatin Password  ab23
    Submit Register
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Go To Register Page
    Set Username  hamidebadi
    Set Password  fdsafasf324
    Set Confirmatin Password  fdsafasb556
    Submit Register
    Register Should Fail With Message  Passwords don't match

Login After Successful Registration
    Go To Register Page
    Set Username  hamidebadi
    Set Password  hamid1234
    Set Confirmatin Password  hamid1234
    Submit Register
    Go To Login Page
    Set Username  hamidebadi
    Set Password  hamid1234
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Go To Register Page
    Set Username  hi
    Set Password  hamid1234
    Set Confirmatin Password  hamid1234
    Submit Register
    Go To Login Page
    Set Username  hi
    Set Password  hamid1234
    Click Button  Login
    Login Page Should Be Open

*** Keywords ***
Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmatin Password
    [Arguments]  ${confirmation}
    Input Text  password_confirmation  ${confirmation}

Submit Register
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${Message}
    Register Page Should Be Open
    Page Should Contain  ${Message}