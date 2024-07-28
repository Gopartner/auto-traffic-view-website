import json
import time
import random
import requests
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from .menu import get_user_input
from .proxy import get_random_proxy
from .user_agent import get_random_user_agent
from .utils import random_wait, random_clicks, random_scroll

# Load configuration
with open('../config/config.json') as config_file:
    config = json.load(config_file)

# Load fake data
with open('../data/fake_data.json') as data_file:
    fake_data = json.load(data_file)

# Get user input
user_input = get_user_input()
url = user_input['url']
proxy = user_input['proxy']
user_agent = user_input['user_agent']

# Fungsi untuk mengakses situs web dengan selenium
def access_website_with_selenium(url, fake_data, proxy, user_agent):
    chrome_options = Options()
    chrome_options.add_argument(f'--proxy-server={proxy}')
    chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument('--headless')  # Jika Anda tidak ingin melihat browser

    driver_service = Service("/path/to/chromedriver")
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)

    try:
        driver.get(url)
        random_wait(3, 5)

        # Tambahkan cookies ke browser
        for key, value in fake_data["cookies"].items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    driver.add_cookie({"name": f"{key}_{sub_key}", "value": str(sub_value)})
            else:
                driver.add_cookie({"name": key, "value": str(value)})

        driver.get(url)  # Reload halaman dengan cookies baru

        # Simulasikan beberapa klik acak dan gulir
        random_clicks(driver)
        random_scroll(driver)

        # Ambil cookies dan kirim permintaan HTTP untuk mempertahankan sesi
        cookies = driver.get_cookies()
        session = requests.Session()
        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'])

        response = session.get(url, headers={"User-Agent": user_agent}, proxies={"http": proxy, "https": proxy})
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text[:200]}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        driver.quit()

# Akses situs web
access_website_with_selenium(url, fake_data, proxy, user_agent)

