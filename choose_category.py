from setUp_driver import setup_driver
from selenium.webdriver.common.by import By
import time

driver = setup_driver()
driver.get("http://localhost/tryingtaleshive/category.html")

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

choose_category("Comedy")
