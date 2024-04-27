from selenium import webdriver
import time


def setup_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=chrome_options)


def highlight_element(driver, element):  # Just to see the element highlighted
    driver.execute_script("arguments[0].setAttribute('style', 'text-decoration: underline;');", element)
    time.sleep(2)
    driver.execute_script("arguments[0].setAttribute('style', '');", element)