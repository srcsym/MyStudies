*** Settings ***
Library  SeleniumLibrary

Resource  ../Resources/PO/LandingPage.robot
Resource  ../Resources/PO/SearchResults.robot
Resource  ../Resources/PO/Product.robot
Resource  ../Resources/PO/Cart.robot
Resource  ../Resources/PO/SignIn.robot
Resource  ../Resources/Po/TopNav.robot



*** Keywords ***

Search for Products
    LandingPage.Load
    LandingPage.Verify Page Loaded
    TopNav.Enter Search Term
    TopNav.Submit Search
    TopNav.Verify Page Loaded

Select Product from Search Results
    SearchResults.Click Product Link
    SearchResults.Verify Page Loaded

Add Product to Cart
    Product.Add to Cart
    Cart.Verify Product Added

Begin Checkout
    Cart.Proceed to Checkout
    Cart.Verify Product Added
    Cart.Proceed to Buy
    SignIn.Verify Page Loaded