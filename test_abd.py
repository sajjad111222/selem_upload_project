import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from allure_commons.types import AttachmentType
import time

def setup_function():
    global driver
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.get("https://dev.alnafi.com/users/sign_in")
    driver.maximize_window()

def teardown_function():
    driver.quit()


def my_credit():
    return [
        ('sajjad1', 'ali123'),
        ('sajjad2', 'eeeee'),
    ]
@pytest.mark.parametrize("username, passwrd", my_credit())
def test_myabd1(username, passwrd):
    driver.find_element(By.ID, 'user[email]').send_keys(username)
    time.sleep(1)
    driver.find_element(By.ID, 'user[password]').send_keys(passwrd)
    time.sleep(1)
    allure.attach(driver.get_screenshot_as_png(), name="my_alnafi_sc", attachment_type=AttachmentType.PNG)


