from setUp_driver import setup_driver
from selenium.webdriver.common.by import By
import time

driver = setup_driver()
driver.get('http://localhost/TryingTaleshive/category.html')

def highlight_element(driver, element): # Just to see the highlighted element
    driver.execute_script("arguments[0].setAttribute('style', 'text-decoration: underline;');", element)
    time.sleep(2)
    driver.execute_script("arguments[0].setAttribute('style', '');", element)


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


for story in test_data:
    read_story(story)
    time.sleep(2)
    driver.back()
    time.sleep(2)

