import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import allure
import logging
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC


@allure.story('进入合约调试')
def into_contract_debug_(driver):
    time.sleep(2)
    driver.find_element(By.XPATH, '//button[text()="Transactions"]').click()
    driver.find_elements(By.XPATH, '//b[text()="Deploy"]')[0].click()
    driver.find_element('css selector', '.text-body').click()


@allure.story('进入合约调试')
def into_contract_debug(driver):
    # 判断合约弹窗，是否进行跳转
    contract_judge = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//div[text()="Contract"]'))
    )
    if contract_judge != "":

        # 合约调试
        print(123)
        driver.find_element('css selector', '.text-body').click()
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//b[text()="approve"]'))
        )
        print("已经进入到合约调试界面~")
        print('已部署成功')
    else:
        print('部署失败或部署超时~~~')
        driver.find_element(By.ID, 'tooltip-build-btn').click()


@allure.story('approve')
def approve(driver):
    # 输入spender的地址
    driver.find_elements('css selector', '.form-control-sm.form-control')[0].send_keys('0x93b23aD298c246f65d64F7E19033C1cCFfde52e2')
    # 输入approve金额
    driver.find_elements('css selector', '.form-control-sm.form-control')[1].send_keys(1)
    driver.find_elements('css selector', '.text-overflow-dots').click()
    driver.find_elements(By.XPATH, '//span[text()="MyWallet"]')
