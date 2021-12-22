*** Settings ***
Library  SeleniumLibrary

*** Keywords ***

Enter Search Term
    Input Text  id=twotabsearchtextbox  Ferrari 458

Submit Search
    Click Button  xpath=//*[@id="nav-search-submit-button"]

Verify Page Loaded
        Wait Until Page Contains  results for "Ferrari 458"