#coding:utf-8
import unittest
import re
import datetime
from time import sleep
from config.selenium_config import selenium_config
import sys
import os
from selenium import webdriver

class Shopping(unittest.TestCase):
    #流程控制
    status_tag = {
        "status": 1
    }
    driver = webdriver.Firefox()

    def __init__(self, methodName):
        super(Shopping,self).__init__(methodName)
    #找不到元素重试
    def driver_process_except(self, driver_process_str, driver = driver, loop_num=5, sleep_time=1):
        if self.status_tag['status'] == 1:
            print 'Current Process : ' + str(driver_process_str).decode('utf-8')
            num = 0
            while num < loop_num:
                try:
                    temp_result =''
                    exec ('temp_result = ' + driver_process_str)
                except Exception, e:
                    print e
                else:
                    break
                finally:
                    num += 1
                    sleep(sleep_time)
            if num == loop_num:
                self.status_tag['status'] = 0
                return False
            else:
                return temp_result
    #检查状态
    def check_process_status(self):
        self.assertEqual(self.status_tag['status'], 1)

    #保存快照
    def save_snapshot(self, name):
        sleep(3)
        date_str = re.sub('[- :]', '', str(datetime.datetime.now()).split('.')[0])
        self.driver_process_except('driver.save_screenshot(r"'+selenium_config['snapshot_path'] + name + '_' + date_str +'.png")')
        #self.driver_process_except('driver.save_screenshot("/Users/vic/work/vic/TW/AutoTestForPython/UI_Testing/snapshot/test.png")')
        #self.driver_process_except('driver.save_screenshot("test.png")')


    #浏览器打开商城
    def Case_1(self):
        '''Purchase book at JingDong website'''
        #self.driver_process_except("http://www.baidu.com")
        #设置窗口大小
        self.driver_process_except('driver.set_window_size(1440, 1200)')
        #打开京东商城
        self.driver_process_except('driver.get("http://www.jd.com/")')
        self.check_process_status()
        #self.save_snapshot("JD_index")

        #输入软件测试后点击搜索
        #self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[1]/input").clear()')
        #self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'search\']/div/div[2]/button").click()')
        self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'key\']").send_keys("软件测试".decode("utf-8"))')
        #self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'key\']").send_keys("软件测试".decode("utf-8"))')
        #self.save_snapshot("step1")
        self.check_process_status()
        sleep(3)
        self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'search\']/div/div[2]/button/i").click()')
        self.check_process_status()
        #找到书籍后进入详情
        sleep(3)
        #self.save_snapshot("step2")
        #self.driver_process_except('driver.find_element_by_xpath("./#//*[@id =\"J_goodsList\"]/ul/li[1]/div/div[3]/a/em/font")').click()
        self.driver_process_except('driver.find_element_by_partial_link_text("软件测试（原书第2版）").click()')
        self.check_process_status()

        #加入购物车
        #self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'InitCartUrl\']").click()')
        self.driver_process_except('driver.find_element_by_partial_link_text("加入购物车").click()')
        self.check_process_status()
        #断言是否加入成功 商品已成功加入购物车！
        #self.assertTrue(self.driver_process_except('driver.find_element_by_partial_link_text("加入购物车")'))
        #self.save_snapshot("step3")
        self.assertTrue(self.driver_process_except('driver.find_element_by_partial_link_text("软件测试（原书第2版）")'))
        #self.assertEqual(self.driver_process_except('driver.find_element_by_partial_link_text("商品已成功加入购物车")'),'成功')
        self.save_snapshot("step4")
        sleep(3)


    def Case_2(self):
        '''Close the browser window'''
        sleep(3)
        self.save_snapshot("step5")
        self.driver_process_except('driver.close()')
        #self.check_process_status()
