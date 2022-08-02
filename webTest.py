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
import os
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import selenium.webdriver.support.ui as ui

import Tools.Build
import Tools.NetworkSwitch
import Tools.Deploy
import Tools.DeleteProject
# from Tools.Build import *

import PageOperation.Contract


@allure.epic('black ide-Web端')
class TestClass:
    @classmethod
    def setup_class(self):
        option = webdriver.ChromeOptions()
        # 添加保持登录的数据路径：安装目录一般在C:\Users\****\AppData\Local\Google\Chrome\User Data
        # option.add_argument(r"user-data-dir=C:\Users\yangw\AppData\Local\Google\Chrome\User Data_Backup")
        self.driver = webdriver.Chrome(options=option)

    # @classmethod
    # def setup_class(self):
    #     chrome_options = webdriver.ChromeOptions()
    #     chrome_options.add_argument('--headless')
    #     chrome_options.add_argument('--no-sandbox')
    #     chrome_options.add_argument('--disable-gpu')
    #     chrome_options.add_argument('--disable-dev-shm-usage')
    #     s = Service('/usr/bin/chromedriver')
    #     self.driver = webdriver.Chrome(service=s, options=chrome_options)
    #     @classmethod
    #     def setup_class(self):
    #         chrome_options = webdriver.ChromeOptions()
    #         chrome_options.add_argument('--headless')
    #         chrome_options.add_argument('--no-sandbox')
    #         chrome_options.add_argument('--disable-gpu')
    #         chrome_options.add_argument('--disable-dev-shm-usage')
    #         # s = Service('/usr/bin/chromedriver')
    #         self.driver = webdriver.Chrome(options=chrome_options)
=======
    # @classmethod
    # def setup_class(self):
    #     option = webdriver.ChromeOptions()
    #     # 添加保持登录的数据路径：安装目录一般在C:\Users\****\AppData\Local\Google\Chrome\User Data
    #     # option.add_argument(r"user-data-dir=C:\Users\yangw\AppData\Local\Google\Chrome\User Data_Backup")
    #     self.driver = webdriver.Chrome(options=option)
#
#     @classmethod
#     def setup_class(self):
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('--headless')
#         chrome_options.add_argument('--no-sandbox')
#         chrome_options.add_argument('--disable-gpu')
#         chrome_options.add_argument('--disable-dev-shm-usage')
#         s = Service('C:\Users\AppData\Local\Google\Chrome\Application\chromedriver.exe')
#         self.driver = webdriver.Chrome(service=s, options=chrome_options)
    @classmethod
    def setup_class(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # s = Service('/usr/bin/chromedriver')
        self.driver = webdriver.Chrome(options=chrome_options)
    @allure.story('打开black ide客户端')
    def test_open(self):
        # try:
        self.driver.get("https://eth-test.ide.black")
        # self.driver.get("https://ide.black")
        logging.info("正在进入web页面~~~")
        # self.driver.find_element('xpath', '//button[@class="btn btn-primary btn-sm")]').click()

        self.driver.implicitly_wait(10)

        self.driver.find_element('css selector', '.button_white.w-button').click()

        self.driver.implicitly_wait(10)

    def visibility_by_xpath(self, xpath_exp):  # 传入元素Xpath进行显式等待，等待可见
        wait = WebDriverWait(self.driver, 20, 0.2)
        wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, xpath_exp)))

    @allure.story('进入github登录页面')
    def test_github_login(self):

        self.driver.find_element('css selector', '.btn.btn-primary.btn-sm').click()

        logging.info("已进入到github登录界面进行登录操作~")
        # assert element, '未进入到github登录页~'

    @allure.story('登录')
    def test_login(self):
        time.sleep(10)
        self.driver.find_element(By.ID, 'login_field').send_keys('WhisperGmail')

        self.driver.find_element(By.ID, 'password').send_keys('12345678dyw')
        self.driver.find_element('css selector', '.btn.btn-primary.btn-block.js-sign-in-button').click()
        time.sleep(10)
        btn = self.driver.find_elements(By.ID, 'js-oauth-authorize-btn')
        if len(btn) == 0:
            logging.info("不存在authorize选项，进行执行")
            # self.driver.find_element('css selector', '.btn.btn-primary.btn-sm.btn-flat').click()
        else:
            logging.info("存在authorize选项，需点击authorize")
            self.driver.find_element(By.ID, 'js-oauth-authorize-btn').click()
        # 等待登录
        time.sleep(15)

        # 点击个人头像
        self.driver.find_element('css selector', '.nav-dropdown-toggle.px-2').click()
        # 点击username
        self.driver.find_element(By.XPATH, '//button[text()="WhisperGmail"]').click()
        # 登录成功后弹框
        loginSuccess = self.driver.find_elements('css selector', '.modal-title')
        # 隐藏弹框
        hidePopUpWindows = self.driver.find_elements('css selector', '.modal-title')
        if len(loginSuccess) != 0:
            logging.info("登录成功！！")
            if len(hidePopUpWindows) != 0:
                self.driver.find_element(By.XPATH, '//button[text()="Cancel"]').click()
                logging.info("存在弹窗，隐藏它~")
            else:
                logging.info("不存在弹窗，进行执行~")
        else:
            logging.info("登录失败")
            # assert loginSuccess, "--------登录失败---------"

    @allure.story('创建密钥对（钱包）')
    def CreateKeyPair(self):
        time.sleep(8)
        self.driver.find_element(By.ID, 'keypair-manager').click()
        self.driver.implicitly_wait(10)
        KeyName = self.driver.find_elements('css selector', '.text-truncate')[0].text
        # 点击密钥对按钮
        # self.driver.find_element('css selector', '.btn.btn-primary.btn-sm.btn-flat').click()
        if KeyName != 'MyWallet':

            # 点击Create
            self.driver.find_element('css selector', '.mr-2.btn.btn-success').click()
            # 输入密钥名称
            self.driver.find_element('css selector', '.form-control').send_keys('MyWallet')
            time.sleep(3)
            # 点击创建
            self.driver.find_element('css selector', '.ml-2.btn.btn-primary').click()
            # 等待创建成功
            time.sleep(5)
            # self.driver.find_element('css selector', '.ml-2.btn.btn-primary').click()
            # 弹窗-信息通知notification-message
            # 判断是否添加密钥对成功
            KeyName = self.driver.find_elements('css selector', '.text-truncate')[0].text
            print(KeyName)
            if KeyName == 'MyWallet':
                logging.info("密钥对添加成功，已在列表内")
                # 隐藏密钥对列表弹窗
                # self.driver.find_element(By.XPATH, '//button[text()="Cancel"]').click()
                # self.driver.find_element('css selector', '.btn.btn-default').click()
            else:
                logging.info("密钥对添加失败")
            assert KeyName, "密钥对添加失败"
        else:
            self.driver.find_element('css selector', '.close').click()
            logging.info("已存在MyWallet钱包，无需再次创建~~")
        self.driver.find_element(By.XPATH, '//div[@text="Create"]').click()

    @allure.story('创建项目-Coin')
    def CreateProject(self):
        time.sleep(8)
        # projectName = self.driver.find_elements(By.XPATH, '//h5[text()="DemoText"]')
        projectname = self.driver.find_elements(By.XPATH, "//h5[text()='Coin']")
        print(projectname)
        if projectname == []:
            time.sleep(5)
            # 点击New，新建项目
            self.driver.find_element('css selector', '.btn.btn-success').click()
            time.sleep(5)
            # 输入项目名称
            self.driver.find_element('css selector', '.form-control').clear()
            self.driver.find_element('css selector', '.form-control').send_keys('Coin')
            time.sleep(5)
            # 点击Create Project
            self.driver.find_element('css selector', '.ml-2.btn.btn-primary').click()
            # self.driver.find_element(By.XPATH, '//button[text()="Create Project"]').click()
        else:
            self.driver.find_element(By.XPATH, "//h5[text()='Coin']").click()
            # TestClass.visibility_by_xpath(self, "//h1[@id='coin']")
            time.sleep(20)
            logging.info("已创建DemoTest,进入该项目~~")

    @allure.story('创建ERC20')
    def test_OpenOrCreate_ERC20(self):
        # 点击个人头像
        time.sleep(8)
        projectname = self.driver.find_elements(By.XPATH, "//h5[text()='ERC-20']")
        print(projectname)
        if projectname == []:
            time.sleep(5)
            # 点击New，新建项目
            self.driver.find_element('css selector', '.btn.btn-success').click()
            time.sleep(5)
            # 输入项目名称
            self.driver.find_element('css selector', '.form-control').clear()
            self.driver.find_element('css selector', '.form-control').send_keys('ERC-20')
            time.sleep(5)
            # select ERC20
            self.driver.find_element(By.XPATH, '//div[text()="Coin"]').click()
            # click ERC20
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button[text()='ERC20 Token']").click()
            # 点击Create Project
            self.driver.find_element('css selector', '.ml-2.btn.btn-primary').click()
            # self.driver.find_element(By.XPATH, '//button[text()="Create Project"]').click()
        else:
            self.driver.find_element(By.XPATH, "//h5[text()='ERC-20']").click()
            # TestClass.visibility_by_xpath(self, "//h1[@id='coin']")
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "erc-20-token"))
            )
            print(element)
            if element != "":
                print("into the project！")
                logging.info("into the project！")
            else:
                print("entry project failure")
                logging.info("entry project failure")
            logging.info("已创建ERC-20,进入该项目~~")
        # 获取到项目类型名称
        projectType = self.driver.find_element('css selector', ".rc-tree-title").text
        print(projectType)
        # Tools.Build.Build(self.driver)
        Tools.NetworkSwitch.Link_Network(self.driver)
        Tools.Deploy.deploy(self.driver)
        PageOperation.Contract.into_contract_debug(self.driver)
        PageOperation.Contract.approve(self.driver)
        # Tools.DeleteProject.delete_Project(self.driver, projectType)



    @allure.story('退出浏览器，清除cookie')
    def Exit_DeleteCookie(self):
        # 清除浏览器cookies
        self.driver.delete_all_cookies()
        self.driver.quit()
    # @allure.story('点击Contract')
    # def test_Contract_Page(self):
    #     self.driver.find_element(By.XPATH, '//*[text()="Contract"]').click()
    #     self.driver.find_elements('css selector', '.nav-dropdown-toggle.p-0.dropdown-toggle')[1].click()
    #
    # @allure.story('点击Explorer')
    # def test_Explorer_Page(self):
    #     self.driver.find_element(By.XPATH, '//*[text()="Explorer"]').click()
    #
    #     self.driver.find_elements('css selector', '.nav-dropdown-toggle.p-0.dropdown-toggle')[2].click()
    #
    # @allure.story('点击Network')
    # def test_Network_Page(self):
    #     self.driver.find_element(By.XPATH, '//*[text()="Network"]').click()
    #     self.driver.find_elements('css selector', '.nav-dropdown-toggle.p-0.dropdown-toggle')[3].click()
    #     self.driver.find_element(By.XPATH, '//*[text()="Ropsten"]').click()

    # @classmethod
    # def teardown_class(cls):
    #     cls.driver.quit()


if __name__ == '__main__':
    pytest.main()
