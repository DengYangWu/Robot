from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
# from selenium.webdriver.common.action_chains import ActionChains
import allure
import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui

@allure.epic('black ide-Web端')
class TestClass:

    @classmethod
    def setup_class(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # # chromedriver = "/usr/bin/chromedriver"
        # chromedriver = "/usr/bin/chromedriver"
        # # 添加保持登录的数据路径：安装目录一般在C:\Users\****\AppData\Local\Google\Chrome\User Data
        chrome_options.add_argument(r"user-data-dir=C:\Users\yangw\AppData\Local\Google\Chrome\User Data_Backup")
        # self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)
        #chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        #chromedriver = "C:\Chromedriver\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    @allure.story('打开black ide客户端')
    def test_open(self):
        # try:
        self.driver.get("https://eth-test.ide.black")
        # self.driver.get("https://ide.black")
        logging.info("正在进入web页面~~~")
        # self.driver.find_element('xpath', '//button[@class="btn btn-primary btn-sm")]').click()

        self.driver.implicitly_wait(10)