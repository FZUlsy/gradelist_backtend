from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


# smtplib模块主要负责发送邮件：是一个发送邮件的动作，连接邮箱服务器，登录邮箱，发送邮件（有发件人，收信人，邮件内容）。
# email模块主要负责构造邮件：指的是邮箱页面显示的一些构造，如发件人，收件人，主题，正文，附件等。

def send(sender_qq, receiver, mail_title, mail_content, auth_code):
    host_server = 'smtp.qq.com'  # qq邮箱smtp服务器

    # 授权码
    # pwd = 'hmqjtysogqskhcid'

    # 初始化一个邮件主体
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq
    # msg["To"] = Header("测试邮箱",'utf-8')
    msg['To'] = receiver

    # 邮件正文内容
    try:
        msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))

        smtp = SMTP_SSL(host_server)  # ssl登录

        smtp.login(sender_qq, auth_code)

        # sendmail(from_addr,to_addrs,msg,...):
        # from_addr:邮件发送者地址
        # to_addrs:邮件接收者地址。字符串列表['接收地址1','接收地址2','接收地址3',...]或'接收地址'
        # msg：发送消息：邮件内容。一般是msg.as_string():as_string()是将msg(MIMEText对象或者MIMEMultipart对象)变为str。
        smtp.sendmail(sender_qq, receiver, msg.as_string())

        # quit():用于结束SMTP会话。
        smtp.quit()
    except Exception as e:
        print(f"邮件发送失败: {e}")
