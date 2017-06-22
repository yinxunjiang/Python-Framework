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
if __name__=='__main__':
    #获取excel表格
    pe = ParseExcel(test_data_excel_path)
    #获取表格的第一个sheet页
    pe.set_sheet_by_index(0)
    #从第二行开始遍历sheet页内容，因为第一行是标题，故忽略
    #id表示遍历的每行的索引号，从0开始
    for id,row in enumerate(pe.get_all_rows()[1:]):
        yes_or_no_execute=row[yes_or_no_num].value
        if yes_or_no_execute=='y':#sheet中是否执行是y时才执行该行数据
            #获取用户名、密码等，列号在var.py文件中已经定义好，这样做阅读清晰
            username=row[username_col_num].value
            password=row[password_col_num].value
            excel_name=row[excel_num].value
            driver = webdriver.Chrome(executable_path="d:\\chromedriver")
            try:
                #调用登录函数
                login(driver, username, password)
                #若运行成功，将结果写入单元格内，定位单元格位置时，行号和列号都是从1开始计算
                pe.write_cell_content(id+2,result_num,'pass')
                #进入邮箱首页
                visit_address_page(driver)
                #new_linkman(driver,u'Bill Gates','764400975@qq.com',u'是','18911734602','new man')
                time.sleep(1)
                #获取包含新建联系人信息的sheet页
                pe.get_sheet_by_name(excel_name)
                try:
                    #遍历该sheet页，从第二行开始
                    for ro in pe.get_all_rows()[1:]:
                        #如果是否执行是y，就将该联系人添加到通讯录
                        if ro[7].value=='y':
                            #调用添加新建联系人的方法
                            new_linkman(driver,ro[1].value,ro[2].value,ro[3].value,ro[4].value,ro[5].value)
                            ro[8].value=date_time_chinese()
                            ro[9].value=u'成功'
                            info('执行成功')
                        else:#如果是否执行是n，则忽略掉该条数据
                            ro[9].value=u'忽略'
                            info('执行成功')
                            ro[9].font= Font(color="FF0000")#设置成红色
                            continue
                    #执行完联系人sheet页内容后，需要重新获取下第一个sheet页，方能执行下一条登录信息
                    pe.set_sheet_by_index(0)
                except Exception,e:
                    ro[8].value=date_time_chinese()
                    ro[9].value=u'失败'
                    error('失败：'+e.message)
                    #执行完联系人sheet页内容后，需要重新获取下第一个sheet页，方能执行下一条登录信息
                    pe.set_sheet_by_index(0)
                    print e.message
            except Exception,e:
                print e.message
                pe.write_cell_content(id + 2, result_num, "fail")
                pe.write_cell_content(id + 2, exception_info_col_no, "fail")
            finally:
                driver.quit()
        #如果是否执行是n，则忽略掉该条数据
        else:
            pe.write_cell_content(id + 2, result_num, u"忽略")
            continue


