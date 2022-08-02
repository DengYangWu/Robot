import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import allure
import logging
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC


@allure.story('删除项目')
def delete_Project(driver, projectType):
    # 点击project settings按钮
    driver.find_element(By.ID, 'toolbar-btn-settings').click()
    # 滚动页面到最底部
    time.sleep(2)
    # 滚动Network下拉菜单
    js = 'document.getElementsByClassName("custom-tab bg2")[0].scrollTop=1000;'
    driver.execute_script(
        js)  # 滚动到底部
    time.sleep(2)
    # click delete button
    driver.find_element(By.XPATH, "//button[text()='Delete Project']").click()
    time.sleep(1)
    # input delete confirm button
    driver.find_element(By.XPATH, '//div/input[@class="form-control"]').send_keys("WhisperGmail/" + projectType)
    # click delete button
    driver.find_element(By.XPATH, "//button[text()='Delete']").click()

    logging.info("项目正在删除中~~~")

    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".media-body"))
    )
    if element != "":
        print("删除项目成功，进入主页")
        logging.info("删除项目成功，进入主页")
    else:
        print("删除项目失败了")
        logging.info("删除项目失败了")
