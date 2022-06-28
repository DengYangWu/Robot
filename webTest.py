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
        chromedriver = "/usr/bin/chromedriver"
        # # 添加保持登录的数据路径：安装目录一般在C:\Users\****\AppData\Local\Google\Chrome\User Data
        # chrome_options.add_argument(r"user-data-dir=C:\Users\yangw\AppData\Local\Google\Chrome\User Data_Backup")
        # self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # chromedriver = "C:\Chromedriver\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)

    @allure.story('打开black ide客户端')
    def test_open(self):
        # try:
        # self.driver.get("https://eth-test.ide.black")
        self.driver.get("https://ide.black")
        logging.info("正在进入web页面~~~")
        # self.driver.find_element('xpath', '//button[@class="btn btn-primary btn-sm")]').click()

        self.driver.implicitly_wait(10)
        # time.sleep(1)
        # search_window = self.driver.current_window_handle  # 此行代码用来定位当前页面
        # blackIcon = self.driver.find_element('css selector','.CircleBadge-icon')
        # self.driver.implicitly_wait(10)  #等待加载

        # assert black_web, '未进入到ide页面~'
        # except:
        #     print("打开了，浏览器~")
        # finally:
        #     self.driver.quit()

    def visibility_by_xpath(self, xpath_exp):  # 传入元素Xpath进行显式等待，等待可见
        wait = WebDriverWait(self.driver, 20, 0.2)
        wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, xpath_exp)))

    @allure.story('进入github登录页面')
    def github_login(self):

        self.driver.find_element('css selector', '.btn.btn-primary.btn-sm').click()
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@class="CircleBadge-icon"]'))
        # )
        self.driver.back()
        logging.info("已进入到github登录界面进行登录操作~")
        # assert element, '未进入到github登录页~'

    @allure.story('登录')
    def login(self):
        time.sleep(5)
        self.driver.find_element('css selector', '.btn.btn-primary.btn-sm.btn-flat').click()
        # githubLogin = self.driver.find_elements('css selector', ".octicon.octicon-mark-github")
        self.driver.find_element(By.ID, 'login_field').send_keys('dengyw1313')
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
        time.sleep(10)
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
        time.sleep(5)
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
        # self.driver.find_element(By.XPATH, '//div[@text="Create"]').click()

    # @allure.story('删除密钥')
    # def test_deleteKeypair(self):
    #     # 点击密钥对按钮
    #     self.driver.find_element('css selector', '.btn.btn-primary.btn-sm.btn-flat').click()
    #     time.sleep(3)
    #     # 双击按钮删除密钥对
    #     #source = self.driver.find_element('css selector', '.far.fa-trash-alt')
    #
    #     # source = self.driver.find_element('css selector', '.far.fa-trash-alt')
    #     # csource = self.driver.find_element(By.XPATH, '//tr[@class="hover-flex"]//td[3]')
    #     mo = self.driver.find_element('css selector', '.small')
    #     ActionChains(self.driver).move_to_element(mo).perform()
    #     #ActionChains(self.driver).double_click(source).perform()
    #     time.sleep(3)
    #     logging.info("删除密钥成功~")

    @allure.story('创建项目-Coin')
    def test_CreateProject(self):
        time.sleep(8)
        projectName = self.driver.find_elements(By.XPATH, '//h5[text()="DemoText"]')
        if projectName == '':
            time.sleep(5)
            # 点击New，新建项目
            self.driver.find_element('css selector', '.btn.btn-success').click()
            time.sleep(5)
            # 输入项目名称
            self.driver.find_element('css selector', '.form-control').clear()
            self.driver.find_element('css selector', '.form-control').send_keys('DemoTest')
            time.sleep(5)
            # 点击Create Project
            self.driver.find_element('css selector', '.ml-2.btn.btn-primary').click()
            # self.driver.find_element(By.XPATH, '//button[text()="Create Project"]').click()
        else:
            self.driver.find_element(By.XPATH, '//h5[text()="DemoText"]').click()
            TestClass.visibility_by_xpath(self, "//h1[@id='coin']")
            # time.sleep(10)
            logging.info("已创建DemoTest,进入该项目~~")

        # 判断项目是否创建成功
        # CoinReadme = self.driver.find_element(By.ID, 'coin').text
        # print(CoinReadme)
        # if CoinReadme == 'Coin':
        #     logging.info('项目已创建成功！！')
        # else:
        #     logging.info('项目已创建失败！！')
        #     assert CoinReadme, '创建项目失败~'

    @allure.story('Coin编译')
    def Build_Coin(self):
        self.driver.find_element(By.ID, 'tooltip-build-btn').click()
        time.sleep(5)
        build = self.driver.find_elements(By.XPATH, '//span[text()="build"]')
        print(build)
        if build != '':
            print('已构建')
        else:
            print('未构建')
            self.driver.find_element(By.ID, 'tooltip-build-btn').click()

    @allure.story('连接网络')
    def test_Link_Network(self):
        self.driver.find_element(By.XPATH, '//*[text()="Network"]').click()
        self.driver.find_elements('css selector', '.nav-dropdown-toggle.p-0.dropdown-toggle')[3].click()
        time.sleep(2)
        # 滚动Network下拉菜单
        self.driver.execute_script(
            "document.getElementsByClassName('dropdown-menu dropdown-menu-right show')[0].scrollTop=600")  # 滚动到底部
        time.sleep(2)
        # 点击conflux测试网
        self.driver.find_element(By.XPATH, "//h6[text()='Conflux espace']/following-sibling::button[2]").click()

        self.driver.find_element('css selector', '.nav-link-content').click()

    @allure.story('部署')
    def test_deploy(self):
        # 点击部署
        time.sleep(5)
        self.driver.find_element(By.ID, 'toolbar-btn-deploy').click()
        time.sleep(5)
        # 点击预估
        self.driver.find_element(By.XPATH, '//button[text()="Estimate & Deploy"]').click()
        # 等待部署后的弹框
        self.driver.implicitly_wait(20)
        # 点击deploy
        self.driver.find_element(By.XPATH, '//button[text()="Deploy"]').click()
        # ele = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, '1')))  # 60s
        self.driver.implicitly_wait(120)

        # wait = WebDriverWait(self.driver, 120, 0.2)
        # wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, "//span[text()='CONFIRMED']")))
        print(123)

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
