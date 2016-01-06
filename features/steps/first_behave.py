from behave import *
import time,os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("I am on BL log in page")
def step_impl(context):

    context.browser.get("https://stagingbluelink.tictrac.com/py_api/api/v1/auth/saml2/test_login/vlad")
    context.browser.maximize_window()


    print("***")

@when("I log in")
def step_impl(context):
    context.browser.find_element_by_id('tt-form-email').send_keys('vlad@tictrac.com')
    context.browser.find_element_by_id('tt-form-password').send_keys('password123')
    context.browser.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/form[2]/div/button').click()
    time.sleep(5)





@then("I see the welcome page")
def step_impl(context):
    assert (context.browser.title) == "Discover - Blue Link"
