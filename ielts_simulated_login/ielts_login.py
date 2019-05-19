# coding = utf-8
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import captcha_recognition

"""
    作者：TimsXH
    功能: 实现雅思网上报名网站的自动登录
    日期：2019-5-19
    version: 0.0.1
"""


class Simulated_Login:

    def __init__(self):
        """
        在self实例上绑定需要的属性
        """
        self.captcha = captcha_recognition.Captcha_Recognition()
        self.browser = Firefox()

    def login(self):
        """
        使用selenium模拟浏览器登陆
        """
        # 1.访问目标登陆页面
        self.browser.get('https://ielts.etest.edu.cn/login')

        # 2.设置延时，直到浏览器渲染出输入框位置,然后获取输入框
        wait = WebDriverWait(self.browser, 10)  # 设置10s延时
        userid = wait.until(
            EC.presence_of_element_located(
                (By.ID, 'userId')))  # 设定筛选规则，通过ID，
        # 阻塞代码运行，直到出现id=‘userId’的标签位置，传入一个元组类型
        passwd = self.browser.find_element_by_id('userPwd')
        # 3. 输入用户名和密码
        userid.send_keys('********')
        passwd.send_keys('********')

        # 4. 获取验证码URL和验证码输入框
        sleep(1)
        captcha_input = wait.until(
            EC.presence_of_element_located(
                (By.ID, 'checkImageCode')))
        captcha = self.browser.find_element_by_id('chkImg')

        # 5.获取验证码标签的URL,解析验证码
        captcha_url = captcha.get_attribute('src')
        print(captcha_url)
        captcha_str = self.captcha.parse(captcha_url)

        # 6.输入验证码 点击登录
        captcha_input.send_keys(captcha_str)
        login_button = self.browser.find_element_by_id('btn_log_goto')
        login_button.click()


def main():
    ielts = Simulated_Login()
    ielts.login()


if __name__ == '__main__':
    main()
