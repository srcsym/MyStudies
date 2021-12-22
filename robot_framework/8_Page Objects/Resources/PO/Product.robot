*** Settings ***
Library  SeleniumLibrary

*** Keywords ***

Add to Cart
    Click Button  xpath=//*[@id="add-to-cart-button"]

Verify Product Added
    Wait Until Page Contains  Added to Cart