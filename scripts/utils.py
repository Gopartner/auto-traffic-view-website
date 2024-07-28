import time
import random
from selenium.webdriver.common.action_chains import ActionChains

def random_wait(min_seconds=1, max_seconds=5):
    time.sleep(random.uniform(min_seconds, max_seconds))

def random_clicks(driver, num_clicks=3):
    for _ in range(num_clicks):
        elements = driver.find_elements_by_xpath("//*")
        if elements:
            element = random.choice(elements)
            try:
                ActionChains(driver).move_to_element(element).click().perform()
                random_wait(1, 3)
            except:
                continue

def random_scroll(driver):
    for _ in range(random.randint(1, 3)):
        scroll_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script(f"window.scrollTo(0, {random.randint(0, scroll_height)});")
        random_wait(1, 3)

