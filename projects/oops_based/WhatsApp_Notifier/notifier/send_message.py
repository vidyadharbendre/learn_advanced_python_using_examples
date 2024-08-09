from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

class WhatsAppNotifier:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None

    def _init_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--user-data-dir=./User_Data")
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get("https://web.whatsapp.com")
        time.sleep(15)  # Wait for manual QR code scan

    def wait_for_login(self):
        while "Login" in self.driver.title:
            time.sleep(1)
        time.sleep(5)  # Wait for WhatsApp Web to fully load

    def send_group_message(self, group_name, message):
        search_box = self.driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.send_keys(group_name)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)

        message_box = self.driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        time.sleep(1)

    def close(self):
        self.driver.quit()
