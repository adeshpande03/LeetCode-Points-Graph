from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import os

def get_session():
    LC_EMAIL = os.environ.get('LC_EMAIL')
    print(LC_EMAIL)
    print(os.environ.get("LC_PASSWORD"))
    url = "https://leetcode.com/accounts/login/"
    driver_path = ChromeDriverManager().install()
    print(driver_path)
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    options.add_argument("--window-size=1920x1080")  # Specify window size
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    print("sleep")
    time.sleep(10)
    login_field = driver.find_element(By.ID, "id_login")
    password_field = driver.find_element(By.ID, "id_password")
    login_field.send_keys(LC_EMAIL)
    password_field.send_keys(os.environ.get('LC_PASSWORD'))
    login_button = driver.find_element(By.ID, "signin_btn")
    print("sleep")
    time.sleep(10.32452345)
    login_button.click()
    print("sleep")
    time.sleep(10)
    cookies = driver.get_cookies()
    print(cookies)
    driver.quit()
    for cookie in cookies:
        if cookie["name"] == "LEETCODE_SESSION":
            return cookie["value"]
        
    return None
