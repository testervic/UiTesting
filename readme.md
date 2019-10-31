# 项目名及简介
* 此项目由Python + nittest + HTMLTestRunner + Selenium等开源工具封装而成的WEB自动化测试工具

# 功能
* 都是基于python2.7（Mac自带）
* 基于Selenium版本2.53.6
* 都是基于webdriver，大部分代码都可以通用，只是配置文件不一样
* 邮件支持多人发送html的测试报告
* 支持多线程
* 支持Chrome和Frefox
* 支持测试截图保存
* 找不到元素重试机制


# 部署步骤
python2.7  //Mac自带
sudo easy_install pip //安装pip
sudo pip install selenium==2.53.6  //安装selenium
(环境搭配selenium2+Firefox46及以下版本兼容，selenium3+Firefox47+geckodriver)

**命名行运行:**

```
python UI_Testing/selenium_index.py
```


# 目录结构描述
```
├── Readme.md                   // help
├── config                      // 配置
├── example                     // demo
│   ├── example_selenium.py     // 元素查找demo
│   ├── example_threading.p     // 多线程并发
├── log                         // 日志存放
├── public                      // 公用方法
│   ├── common                  
│       ├── date.py             // 时间处理
│       ├── file.py             // 获取文件时间
│       ├── log.py              // 日志处理
│       ├── sendEmail.py        // 邮件处理
│   ├── report
│       ├── report_currency.py  // html报告格式
│   ├── selenium_test           // 启动日志配置
│       ├── ProjectCase         // 项目文件
│           ├── Shopping.py     // 被测项目case写在这里
│       ├── selenium_common.py  // 用例执行
│   ├── mysql_handle.py         // 数据库配置
├── report                      // 存放测试报告
├── snapshot                    // 存放测试截图
├── selenium_index.py           // 入口
```


# V1.0.0 版本内容更新

TW面试作业


