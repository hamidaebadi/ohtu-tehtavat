*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User
*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  testUser  admin1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  Hamid  hamid1234
    Output Should Contain  User with username Hamid already exists

Register With Too Short Username And Valid Password
    Input Credentials  ha  hamid1234
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  testUser  ab
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  haebadi  thisispass
    Output Should Contain  Password should also include digits
*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  Hamid  hamid1234
    