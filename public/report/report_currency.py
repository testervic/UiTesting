#coding:utf-8
from config.report_config import *
from public.common.log import *

#html中报告包含表单数据展示，value_list为待展示数据列表，最高支持三维，set_num为是否展示序号列，0为不展示
def set_table_value(value_list, set_num = 0):
    #展示数据列表为空时，返回0
    if type(value_list) == list:
        if len(value_list) == 0:
            logging.info('数据列表为空！')
            return 0
        else:
            html_str = ''
            # 第一维处理
            for i in range(0,len(value_list)):
                #序号处理
                if set_num == 1:
                    html_str += '<tr><td>' + str(i + 1) + '</td>'
                else:
                    html_str += '<tr>'

                if type(value_list[i]) != list:
                    html_str += '<td>' + str(value_list[i]) + '</td>'
                else:
                    #第二维处理
                    if len(value_list[i]) > 0:
                        for j in range(0,len(value_list[i])):
                            html_str += '<td>'
                            if type(value_list[i][j]) != list:
                                html_str += str(value_list[i][j])
                            else:
                                #第三维处理
                                if len(value_list[i][j]) > 0:
                                    for k in range(0,len(value_list[i][j])):
                                        html_str += '<li>' + str(value_list[i][j][k]) + '</li>'
                            html_str += '</td>'
                html_str += '</tr>'
            return html_str
    else:
        logging.warning('数据列表提交错误，应为列表类型数据！')
        return 0

class html_report():

    def __init__(self):
        self.html = ''
        self.style = ''
        self.title = '测试报告'
        self.meta = r'<meta http-equiv="Content-type" content="text/html; charset=utf-8" />'
        self.body = ''
        self.table = ''
        self.div = ''

    def set_style(self, style_config):
        self.style = '<style>' + str(style_config) + '</style>'

    def set_head(self):
        self.head = '<head>' + self.meta + self.title + '</head>'

    def set_table(self, table):
        self.table = table

    def set_body(self):
        pass

    def set_div(self):
        pass

    def set_content(self):
        pass

    def create_html(self):
        pass