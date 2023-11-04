from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

def send_email(sender_email, recipient_email, mail_content):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = Header("dasdas",'utf-8')

    #qq邮箱smtp服务器
    host_server = 'smtp.qq.com'  

    #授权码
    pwd = 'hmqjtysogqskhcid'
    # 连接到SMTP服务器并发送邮件
    try:
        msg.attach(MIMEText(mail_content,'plain','utf-8'))

        smtp = SMTP_SSL(host_server) # ssl登录

        smtp.login(sender_email,pwd)

        # sendmail(from_addr,to_addrs,msg,...):
        # from_addr:邮件发送者地址
        # to_addrs:邮件接收者地址。字符串列表['接收地址1','接收地址2','接收地址3',...]或'接收地址'
        # msg：发送消息：邮件内容。一般是msg.as_string():as_string()是将msg(MIMEText对象或者MIMEMultipart对象)变为str。

        smtp.sendmail(sender_email,recipient_email,msg.as_string())
        smtp.quit()
    except Exception as e:
        print(f"邮件发送失败: {e}")
