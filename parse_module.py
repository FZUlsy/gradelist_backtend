# -*- coding = utf-8 -*-
# @Time : 2023-11-4 14:23
# @Author : Lurume
# @File : parse_module.py
# @Software : PyCharm
import sqlite3

import pandas as pd
from flask import Flask, request
from flask_cors import cross_origin

import email_module as emailModule

app = Flask(__name__)


@app.route('/receive', methods=['POST'])
@cross_origin()
def receive():
    uploaded_file = request.files['file']

    try:
        if uploaded_file.filename != '':
            uploaded_file.save('gradelist.xlsx')
            df = pd.read_excel('gradelist.xlsx')
            print(df)
            result = generate_notice(df)
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
            message += f"{key}:{value}。"
        message += "\n希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。如果您在某些科目上没有达到预期的成绩，不要灰心，这也是学习过程中的一部分。我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。" \
                   "再次恭喜您，祝您学习进步、事业成功！" \
                   "教务处"
        total[name] = message

    for key, value in total.items():
        try:
            email = query_database(key)
            if email:
                emailModule.send('1159210595@qq.com', email[0], '成绩单', value)
        except Exception as e:
            emailModule.send('1159210595@qq.com', '1131288411@qq.com', '成绩单', value)

    return {"message": "success", "data": total}
