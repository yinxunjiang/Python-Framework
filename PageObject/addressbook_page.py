#encoding=utf-8
import time
from Util.ObjectMap import *
from Util.PageObjectRepostory import ParsePageObjectRepositoryConfig
from Action.login import *
from Action.visit_home_page import *
class Address(object):
    u''' 此类定义了获取邮箱主页面各元素的方法，如通讯录，新建联系人等 '''
    def __init__(self,driver):
        self.driver=driver
        self.parse_config_file=ParsePageObjectRepositoryConfig()
        self.login_page_items=self.parse_config_file.getItemsFromSection("126mail_addContactsPage")
        #print self.login_page_items
    #获取新建联系人元素
    def get_add_linkman(self):
        locateType,locateExpression=self.login_page_items['addcontacts_page.createcontactsbtn'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType,locateExpression)
    #获取姓名元素
    def get_name(self):
        locateType,locateExpression=self.login_page_items['addcontacts_page.contactpersonname'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType,locateExpression)
    #获取邮箱元素
    def get_email(self):
        locateType,locateExpression=self.login_page_items['addcontacts_page.contactpersonemail'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType,locateExpression)
    #获取设为星标联系人元素
    def get_star(self):
        locateType,locateExpression=self.login_page_items['addcontacts_page.starcontacts'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType,locateExpression)
    #获取手机号码元素
    def get_phone(self):
        locateType,locateExpression=self.login_page_items['addcontacts_page.contactpersonmobile'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType,locateExpression)
    #获取备注元素
    def get_remark(self):
        locateType,locateExpression=self.login_page_items['addcontacts_page.contactpersoncomment'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType,locateExpression)
    #获取确定元素
    def get_ok(self):
        locateType,locateExpression=self.login_page_items['addcontacts_page.savecontaceperson'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType,locateExpression)



if __name__=="__main__":
    from selenium import  webdriver
    from Action.login import *
    driver = webdriver.Chrome(executable_path="d:\\chromedriver")
    login(driver,'yinxunjiang123','gloryroad')
    visit_address_page(driver)
    lp=Address(driver)
    print lp.addressbook()

