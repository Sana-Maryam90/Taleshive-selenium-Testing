from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('http://localhost/TryingTaleshive/login.html')
# element = driver.find_element(By.CSS_SELECTOR , "a[href='category.html']")
#
#
# # elem = driver.find_element(By.CLASS_NAME, "shop")
# element.click()
#
# product = driver.find_element(By.CLASS_NAME, "product")
# product.click()


def test_login(email, password):
    username_input = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
    password_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")

    username_input.send_keys(email)
    time.sleep(1)  # Wait for 1 second
    password_input.send_keys(password)
    time.sleep(1)  # Wait for 1 second
    submit_button.click()


def choose_category(category):
    category_button = driver.find_element(By.ID, category)
    category_button.click()

    stories = driver.find_elements(By.CLASS_NAME, 'product')
    count = 0

    for story in stories:
        title = story.find_element(By.CSS_SELECTOR, '.title h4').text

        story.click()
        categories = driver.find_element(By.ID, "categ")
        time.sleep(1)
        if category.lower() in categories.text:
            print(title, " belongs to ", category, " category")
            count += 1

        driver.back();
        time.sleep(1)

    if count == len(stories):
        print("All stories belong to ", category, " category")
        print("Test Passed!")
    else:
        print("Category Selection failed")


# login = driver.find_element(By.CLASS_NAME, "loginpopup")
# login.click()
#
# test_login("sana123@html.com", "abcdefgh")


def go_to_workspace():
    profile = driver.find_element(By.CLASS_NAME, "profile-icon")
    profile.click()
    time.sleep(1)  # Wait for 1 second

    workspace = driver.find_element(By.CLASS_NAME, "workspace")
    workspace.click()


# go_to_workspace()


def read_story(title):
    # read_button = driver.find_element(By.CSS_SELECTOR, "a[href='category.html']")
    # read_button.click()
    path = f"//h4[contains(text(), '{title}')]"
    story = driver.find_element(By.XPATH, path)
    story.click()


def write_comment(name, comment):
    name_input = driver.find_element(By.CLASS_NAME, "n-input")
    name_input.send_keys(name)
    comment_input = driver.find_element(By.CLASS_NAME, "comment-input")
    comment_input.send_keys(comment)
    submit_button = driver.find_element(By.CLASS_NAME, "comment-button")
    submit_button.click()


def write_story():
    title = driver.find_element(By.ID, "title-input")
    title.send_keys("Testing Story")
    time.sleep(1)  # Wait for 1 second
    content = driver.find_element(By.CLASS_NAME, "ql-editor")
    content.send_keys("This is our testing content")

    genre1 = driver.find_element(By.CSS_SELECTOR, "input[value='comedy']")
    genre1.click()

    time.sleep(1)  # Wait for 1 second

    genre2 = driver.find_element(By.CSS_SELECTOR, "input[value='thriller']")
    genre2.click()

    time.sleep(1)  # Wait for 1 second
    button = driver.find_element(By.ID, "publish-button")
    button.click()

# write_story()

# driver.back();
# driver.back();
# driver.back();



element = driver.find_element(By.CSS_SELECTOR, "a[href='category.html']")
element.click()

time.sleep(1)
choose_category("Comedy")
# time.sleep(1)
# # read_story("Testing Story")
# read_story("Family Drama")
#
# time.sleep(1)
# write_comment("madMan", "This is the stupidest decision I've ever made")
# time.sleep(5)
# driver.refresh()
#
# # time.sleep(10)
# # driver.quit()
