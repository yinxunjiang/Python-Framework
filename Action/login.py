#encoding=utf-8
from selenium import webdriver
import time
from PageObject.addressbook_page import *
from PageObject.login_page import *
from Util.Excel import *
from ProjectVar.var import *
''' 此模块定义了登录操作，通过执行它可实现登录  '''

def login(driver,username, password):
    #global driver
    #driver=webdriver.Chrome(executable_path="d:\\chromedriver")
    driver.get("http://mail.126.com")
    time.sleep(4)
    lp = LoginPage(driver)
    driver.switch_to.frame(lp.frame())
    time.sleep(2)
    lp.username().send_keys(username)
    lp.password().send_keys(password)
    lp.loginbutton().click()
    time.sleep(3)
    #driver.quit()


if __name__=='__main__':
    '''
    #path=os.path.join(project_path,'testdata',u"126邮箱联系人.xlsx")
    pe=ParseExcel(test_data_excel_path)
    pe.get_sheet_by_name(u"126账号")
    for row in pe.get_all_rows()[1:]:
        username=row[1].value
        password=row[2].value
        dataexcel=row[3].value
        yes_or_no_execute=row[4].value
        try:
            if yes_or_no_execute=='y':
                login(driver,username,password)
                row[5].value=u'成功'
        except Exception,e:
            row[5].value=u'失败'
    pe.workbook_save()
    '''
    '''
    for id,row in enumerate（pe.get_all_rows()[1:]）:
    第一次循环:id；0  row:第二行
        writecell函数，咱们自己封装的，写单元格：从1开始写
        writecell(id+2,5,"pass")
        第二次循环：id:1  row:第三行
        writecell(id+2,5,"pass")
    '''
    driver=webdriver.Chrome(executable_path="d:\\chromedriver")
    login(driver, "testman1980", "wulaoshi1978")


