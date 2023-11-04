import pandas as pd

def import_grades(file_path):
    # 导入成绩表
    try:
        grades = pd.read_csv(file_path)
        return grades
    except FileNotFoundError:
        print("文件不存在，请检查文件路径。")
         return None

 def generate_report(grades):
     # 生成成绩单
     report = grades.groupby('姓名')['成绩'].mean().reset_index()
     return report

 def send_email(subject, message, from_email, password, to_email):
     # 发送邮件
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

     msg.attach(MIMEText(message, 'plain'))

     try:
         server = smtplib.SMTP('smtp.gmail.com', 587)
         server.starttls()
         server.login(from_email, password)
         server.send_message(msg)
         server.quit()
         print("邮件发送成功。")
     except:
         print("邮件发送失败，请检查邮箱设置。")

 def main():
     print("欢迎使用成绩管理系统！")

     while True:
        print("\n请选择操作：")
      print("1. 导入成绩表")
         print("2. 生成成绩单")
         print("3. 发送成绩单通知邮件")
      print("4. 退出程序")

         choice = input("请输入操作编号：")

         if choice == '1':
             file_path = input("请输入成绩表文件路径：")
             grades = import_grades(file_path)
            if grades is not None:
                 print("成绩表导入成功。")

         elif choice == '2':
             if 'grades' in locals():
                 report = generate_report(grades)
                 print("成绩单生成成功。")
                 print(report)
            else:
                 print("请先导入成绩表。")

         elif choice == '3':
             if 'grades' in locals():
                from_email = input("请输入发件人邮箱：")
                 password = input("请输入发件人邮箱密码：")
                 to_email = input("请输入收件人邮箱：")
                subject = input("请输入邮件主题：")
                 message = input("请输入邮件内容：")
                 send_email(subject, message, from_email, password, to_email)
             else:
                print("请先导入成绩表。")

         elif choice == '4':
            print("感谢使用成绩管理系统，再见！")
             break

         else:
             print("无效的操作，请重新输入。")

 if __name__ == "__main__":
    main()
