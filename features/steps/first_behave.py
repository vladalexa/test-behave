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
    passw=open('.\\resources\\pass.txt','r')
    actions = ActionChains(context.browser)
    actions.send_keys("vlad")
    actions.send_keys(Keys.TAB)
    actions.send_keys(passw.readline())
    actions.send_keys(Keys.ENTER)
    actions.perform()

    try:
        element = WebDriverWait(context.browser, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.ng-scope > div.page.page--with-masthead.ng-scope > div > nav > ul:nth-child(1) > li:nth-child(2) > a > div > span"))
    )
        element.click()
        time.sleep(2)
    except Exception:
        print('error')




@then("I see the welcome page")
def step_impl(context):
    assert (context.browser.title) == "Discover - Blue Link"
