*** Settings ***
Resource  ../Resources/scope.robot
*** Variables ***
#${MY_VARIABLE} =  From the script file

*** Test Cases ***

Create and log a variable
    #${my_variable} =  Set Variable  some information
    log  ${MY_VARIABLE}

Access a variable
    Log  ${MY_VARIABLE}


*** Keywords ***