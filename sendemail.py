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
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
    smtpObj.login(mail_user, mail_pass)  # 登录验证
    #发送
    smtpObj.sendmail(
        sender,receivers,message.as_string())
    #退出
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('error',e) #打印错误
