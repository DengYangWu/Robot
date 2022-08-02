import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import allure
import logging
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC


@allure.story('连接网络')
def Link_Network(driver):
    # 点击Network下拉菜单
    driver.find_element(By.XPATH, '//*[text()="Network"]').click()
    driver.find_elements('css selector', '.nav-dropdown-toggle.p-0.dropdown-toggle')[3].click()
    time.sleep(2)
    # 滚动Network下拉菜单
    driver.execute_script(
        "document.getElementsByClassName('dropdown-menu dropdown-menu-right show')[0].scrollTop=600")  # 滚动到底部
    time.sleep(2)
    # 点击conflux测试网
    driver.find_element(By.XPATH, "//h6[text()='Conflux espace']/following-sibling::button[2]").click()

    driver.find_element('css selector', '.nav-link-content').click()
