from common_functions import setup_driver, highlight_element
from selenium.webdriver.common.by import By
import time

driver = setup_driver()
driver.get('http://localhost/TryingTaleshive/category.html')

test_data = ['art of story telling', r"a prisoner's apostasy", "The Tale of Two Sisters"]


def read_story(title):
    path = f'//h4[contains(text(), "{title}")]'
    story = driver.find_element(By.XPATH, path)
    story.click()

    story_title = driver.find_element(By.ID, "title")
    if story_title.text == title:
        highlight_element(driver, story_title)
        print("Title requested: ", title, " , ", "Title opened: ", story_title.text)
        print("Test case Passed!")
    else:
        print("Title requested: ", title, " , ", "Title opened: ", story_title.text)
        print("Test case Failed!")


# Executing tests with different story titles
for story in test_data:
    read_story(story)
    time.sleep(2)
    driver.back()
    time.sleep(2)

