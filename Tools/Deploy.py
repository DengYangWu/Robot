import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import allure
import logging
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC

@allure.story('部署')
def deploy(driver):
    # 点击部署
    driver.find_element(By.ID, 'toolbar-btn-deploy').click()
    time.sleep(2)
    # 点击预估
    driver.find_element(By.XPATH, '//button[text()="Estimate & Deploy"]').click()
    # 等待部署后的弹框
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="Deploy"]'))
    )
    if element != "":
        # 点击deploy
        driver.find_element(By.XPATH, '//button[text()="Deploy"]').click()

        contract_judge = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='CONFIRMED']"))
        )
        if contract_judge != "":

            # 点击关闭弹窗
            # driver.find_element(By.XPATH, "//button[text()='Close']").click()
            print('已部署成功')
        else:
            print('部署失败或部署超时~~~')
            driver.find_element(By.ID, 'tooltip-build-btn').click()

    else:
        print('未部署成功')
        driver.find_element(By.ID, 'tooltip-build-btn').click()