# -*- coding = utf-8 -*-
# @Time : 2023-11-4 14:23
# @Author : Lurume
# @File : parseModule.py
# @Software : PyCharm
import os
import sqlite3
import time

import pandas as pd
from flask import Flask, request
from flask_cors import cross_origin

import emailModule as emailModule

app = Flask(__name__)


@app.route('/receive', methods=['POST'])
@cross_origin()
def receive():
    uploaded_file = request.files['file']
    timestamp = int(time.time())
    try:
        if uploaded_file.filename != '':
            # 获取当前时间戳
            uploaded_file.save(f'{timestamp}.xlsx')
            df = pd.read_excel(f'{timestamp}.xlsx')

            # print(df)
            result = generate_notice(df)

            # 删除文件
            os.remove(f'{timestamp}.xlsx')
            return result
    except Exception as e:
        return {"message": "error", "data": str(e)}


def query_database(stu_name):
    # 通过姓名查询邮箱
    conn = sqlite3.connect('./stuinfo.db')
    cur = conn.cursor()
    try:
        sql = f"select email from studentInfo where stu_name='{stu_name}'"
        cur.execute(sql)
        result = cur.fetchone()
        return result
    except Exception as e:
        print(e)
        return None


def generate_notice(dataframe):
    # 检查第二行的列名是否正确
    # 选课时间  学号	姓名	课程名称	学分	百分成绩	五分成绩	考试类型	选修类型
    if dataframe.iloc[0, 0] != "选课时间" or dataframe.iloc[0, 1] != "学号" or dataframe.iloc[0, 2] != "姓名" or \
            dataframe.iloc[0, 3] != "课程名称" or dataframe.iloc[0, 4] != "学分" or dataframe.iloc[
        0, 5] != "百分成绩" or dataframe.iloc[0, 6] != "五分成绩" or dataframe.iloc[0, 7] != "考试类型" or \
            dataframe.iloc[0, 8] != "选修类型":
        return {"message": "error", "data": "列名错误"}

    name_id = dataframe.iloc[1:, 2:3]
    name_id = set(name_id.values.flatten())

    total = {}
    # 根据姓名提取成绩
    for name in name_id:
        score = dict()
        for index, row in dataframe.iterrows():
            if row[2] == name:
                score[(row[3])[1:]] = "百分成绩:" + str(row[5]) + ",五分成绩:" + str(row[4])
        message = f"亲爱的{name}同学:\n祝贺您顺利完成本学期的学习！教务处在此向您发送最新的成绩单。\n"
        for key, value in score.items():
            message += f"{key}:{value}。\n"
        message += "\n希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。如果您在某些科目上没有达到预期的成绩，不要灰心，这也是学习过程中的一部分。我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。" \
                   "再次恭喜您，祝您学习进步、事业成功！" \
                   "教务处"
        total[name] = message

    for key, value in total.items():
        try:
            email = query_database(key)
            if email:
                emailModule.send('1159210595@qq.com', email[0], '成绩单', value, 'hmqjtysogqskhcid')
        except Exception as e:
            emailModule.send('1159210595@qq.com', '1131288411@qq.com', '成绩单', value, 'hmqjtysogqskhcid')

    return {"message": "success", "data": total}
