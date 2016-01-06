from behave import *
import testlink
import time,os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("I am on BL log in page")
def step_impl(context):

    context.browser.get("https://staging1d.tictrac.com")
    context.browser.maximize_window()


    print("***")

@when("I log in")
def step_impl(context):
    passw=open('C:\\Projects\\tictrac-bahave\\tictrac-qa\\tictrac-behave\\pass.txt','r')
    context.browser.find_element_by_id('tt-form-email').send_keys('vlad@tictrac.com')
    context.browser.find_element_by_id('tt-form-password').send_keys(passw.readline())
    context.browser.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div[1]/form[2]/div/button').click()
    time.sleep(5)

    # try:
    #     element = WebDriverWait(context.browser, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.ng-scope > div.page.page--with-masthead.ng-scope > div > nav > ul:nth-child(1) > li:nth-child(2) > a > div > span"))
    # )
    #     element.click()
    #     time.sleep(2)
    # except Exception:
    #     print('error')




@then("I see the welcome page")
def step_impl(context):
    assert (context.browser.title) == "Discover - Blue Link"