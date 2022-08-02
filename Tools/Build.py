import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import allure
import logging
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC


@allure.story('Coin编译')
def Build(driver):
    # 点击Build按钮
    driver.find_element(By.ID, 'tooltip-build-btn').click()

    # 等待Build文件夹出现
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='build']"))
    )

    if element != "":
        print('已build')
    else:
        print('未build')
        driver.find_element(By.ID, 'tooltip-build-btn').click()
