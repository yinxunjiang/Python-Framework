#encoding=utf-8
import time
from Util.ObjectMap import *
from Util.PageObjectRepostory import ParsePageObjectRepositoryConfig

class LoginPage(object):
    u''' 此类定义了获取登录页面所需元素的方法，包括进入frame，获取用户名、密码、登录按钮 '''
    def __init__(self,driver):
        self.driver=driver
        self.parse_config_file=ParsePageObjectRepositoryConfig()
        self.login_page_items=self.parse_config_file.getItemsFromSection(
            "126mail_login")
        print self.login_page_items

    def frame(self):
        locateType, locateExpression = self.login_page_items['login_page.frame'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def username(self):
        locateType,locateExpression=self.login_page_items['login_page.username'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType,locateExpression)

    def password(self):
        locateType,locateExpression=self.login_page_items['login_page.password'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType,locateExpression)

    def loginbutton(self):
        locateType,locateExpression=self.login_page_items['login_page.loginbutton'].split(">")
        #print locateType, locateExpression
        return getElement(self.driver, locateType,locateExpression)

if __name__=="__main__":
    from selenium import webdriver
    driver=webdriver.Chrome(executable_path="d:\\chromedriver")
    lp=LoginPage(driver)
    lp.username()
    lp.password()
    lp.loginbutton()

