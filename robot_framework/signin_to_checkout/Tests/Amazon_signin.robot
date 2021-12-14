*** Settings ***
Documentation  This is some basic info about the whole suite
Library  SeleniumLibrary

*** Variables ***


*** Test Cases ***
User must sign in to check out
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke
    Open Browser  http://www.amazon.com     gc
    Sleep  3s
    Input Text  id=twotabsearchtextbox    Ferrari 458
    Sleep  3s
    Click Button  xpath=//*[@id="nav-search-submit-button"]
    Sleep  3s
    Click Link  xpath=//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/span/div/div/div[2]/div[1]/h2/a
    Sleep  3s
    Click Button  xpath=//*[@id="add-to-cart-button"]
    Sleep  3s
    Click Link  xpath=//*[@id="nav-cart"]
    Sleep   3s
    Click Button  xpath=//*[@id="sc-buy-box-ptc-button"]/span/input
    Sleep  3s
    Page Should Contain  Sign-In
    Sleep  3s
    Close Browser