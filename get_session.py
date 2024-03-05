from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import os

def get_session():
    LC_EMAIL = os.environ.get('LC_EMAIL')
    url = "https://leetcode.com/accounts/login/"
    driver_path = ChromeDriverManager().install()
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    options.add_argument("--window-size=1920x1080")  # Specify window size
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    time.sleep(5)
    login_field = driver.find_element(By.ID, "id_login")
    password_field = driver.find_element(By.ID, "id_password")
    login_field.send_keys(LC_EMAIL)
    password_field.send_keys(os.environ.get('LC_PASSWORD'))
    login_button = driver.find_element(By.ID, "signin_btn")
    time.sleep(3.5463)
    login_button.click()
    time.sleep(3)
    cookies = driver.get_cookies()
    driver.quit()
    for cookie in cookies:
        if cookie["name"] == "LEETCODE_SESSION":
            return cookie["value"]
        
    return None
