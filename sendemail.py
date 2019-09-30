import smtplib
from email.mime.text import MIMEText
#设置服务器所需信息

#163邮箱服务器地址
mail_host = 'smtp.163.com'
#163用户名
mail_user = 'flypython***'
#密码(163等邮箱为授权码)
mail_pass = '7******x'

#发送地址
sender = 'flypython.com'
#发送内容为纯文本
message = MIMEText('Hello World ! This is from FlyPython!','plain','utf-8')
#email主题
message['Subject'] = 'FlyPython'
#发送地址
message['From'] = sender
#接受地址
receivers = ['flypython.com@gmail.com']
#接受地址的名称
message['To'] = ['flypython.com@gmail.com']


#登录并发送邮件
try:
    smtpObj = smtplib.SMTP()
    #连接到服务器
    smtpObj.connect(mail_host,25)
    #登录到服务器
    smtpObj.login(mail_user,mail_pass)
    #发送
    smtpObj.sendmail(
        sender,receivers,message.as_string())
    #退出
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('error',e) #打印错误