from common_functions import setup_driver
from selenium.webdriver.common.by import By
import time

driver = setup_driver()
driver.get('http://localhost/TryingTaleshive/login.html')


def go_to_workspace():
    profile = driver.find_element(By.CLASS_NAME, "profile-icon")
    profile.click()
    time.sleep(1)

    if driver.find_element(By.CSS_SELECTOR, ".alert.active"):
        print("Only Logged-in users can access workspace")
    else:
        workspace = driver.find_element(By.CLASS_NAME, "workspace")
        workspace.click()

# go_to_workspace()
def execute_test():
    print("Try to access workspace without login")
    go_to_workspace()

    time.sleep(4)
    print("Try to access workspace after login")
    login("sana123@html.com", "abcdefgh")
    go_to_workspace()
