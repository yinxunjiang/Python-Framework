#encoding=utf-8
from selenium import webdriver
from Util.log import *
from Util.FormatTime import *
from Util.Excel import *
import time
from Action.addressbook import *
from Action.login import *
from Action.visit_home_page import *
from ProjectVar.var import *

pe = ParseExcel(test_data_excel_path)
pe.set_sheet_by_index(0)
for id,row in enumerate(pe.get_all_rows()[1:]):
    yes_or_no_execute=row[yes_or_no_num].value
    if yes_or_no_execute=='y':
        username=row[username_col_num].value
        password=row[password_col_num].value
        driver = webdriver.Chrome(executable_path="d:\\chromedriver")
        try:
            login(driver, username, password)
            visit_address_page(driver)
            new_linkman(driver,u'Bill Gates','764400975@qq.com',u'是','18911734602','new man')
            time.sleep(3)
            pe.write_cell_content(id+2,result_num,'pass')
        except Exception,e:
            print e.message
            pe.write_cell_content(id + 2, result_num, "fail")
            pe.write_cell_content(id + 2, exception_info_col_no, "fail")
        finally:
            driver.quit()
    else:
        pe.write_cell_content(id + 2, result_num, u"忽略")
        continue
