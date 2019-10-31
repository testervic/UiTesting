#coding:utf-8

email_config = {
    #发件人
    "sender" : 'zw.vic@qq.com',
    #收件人,多个收件人按;隔开
    "receiver" : 'zw.vic@qq.com',
    #邮件发送服务器
    "smtpserver" : 'smtp.qq.com',
    #发件人账号
    "username" : 'zw.vic@qq.com',
    #发件人密码
    "password" : '',
    #邮件标题
    "mail_title" : '自动化测试报告',
    #邮件内容
    "mail_body" : '测试一下邮件到达情况',
    #附件,list
    "attachment": ['HTMLReport.html',r'F:\work\aaaa\test.txt']
}