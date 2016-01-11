from behave import *
import time,os
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("I am on the {env_selected} login page")
def step_impl(context,env_selected):
    
    context.browser.get('http://www.google.com')
    context.browser.maximize_window()

@when("I click on {element} element")
def step_impl(context,element):
    option = {
        "Signup_confirm": "//form[@name='authForm']/div/button",
        "Signup": "//div[@class='auth-form__footer']/p/a",
        "Cancel": "//button[@analytics-label='cancel']"
    }
    r=requests.get('http://google.com')
    link = context.browser.find_element_by_xpath(option.get(element))
    link.click()
    context.execute_steps(u"""
    then I wait 5 seconds
    """)

@then("I wait {number:d} seconds")
def step_impl(context,number):
    time.sleep(number)

@then("I can see the {page_name} page")
def step_impl(context,page_name):
    option = {
        "Signup": "Sign up",
        "Onboarding": "Onboarding"
    }
    assert (context.browser.title) == option.get(page_name)

@when("I sign up with the credentials: {login}, {password}")
def step_impl(context,login,password):
    ts=str(time.time())
    new_login = ts+login
    print(new_login)
    context.browser.find_element_by_id('tt-form-email').send_keys(new_login)
    context.browser.find_element_by_id('tt-form-password').send_keys(password)
    context.browser.find_element_by_id('tt-form-confirmPassword').send_keys(password)
    context.browser.find_element_by_xpath("//form[@name='authForm']/div/button").click()
    context.execute_steps(u"""
    then I wait 5 seconds
    """)
