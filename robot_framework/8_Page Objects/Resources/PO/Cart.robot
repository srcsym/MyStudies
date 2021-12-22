*** Settings ***
Library  SeleniumLibrary

*** Keywords ***

Proceed to Checkout
    Click Link  xpath=//*[@id="nav-cart"]

Verify Product Added
    Wait Until Page Contains  Shopping Cart

Proceed to Buy
    Click Button  xpath=//*[@id="sc-buy-box-ptc-button"]/span/input



