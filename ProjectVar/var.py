#encoding=utf-8
import os
#打印文件所在目录
file_path=os.path.dirname(__file__)
#打印文件所在的工程目录
project_path=os.path.dirname(os.path.dirname(__file__))
#测试数据路径
test_data_excel_path=os.path.join(project_path,'testdata',u"126邮箱联系人.xlsx")
#test_data_excel_path=project_path+u"/testdata/126邮箱联系人.xlsx"
#获取页面元素配置文件路径
configFilePath=os.path.join(project_path,'conf','PageElementLocator.ini')
#excel表格获取用户名、密码
username_col_num=1
password_col_num=2
excel_num=3
yes_or_no_num=4
result_num=6
exception_info_col_no=7

if __name__=='__main__':
    print file_path
    print project_path
    print test_data_excel_path
    print configFilePath
