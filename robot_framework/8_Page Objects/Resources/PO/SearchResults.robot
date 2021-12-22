*** Settings ***
Library  SeleniumLibrary

*** Keywords ***

Click Product Link
    Click Link  xpath=//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/span/div/div/div[2]/div[1]/h2/a

Verify Page Loaded
    Wait Until Page Contains  Back to results