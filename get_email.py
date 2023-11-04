import pandas as pd

# 指定成绩表文件路径
file_path = r'C:\Users\Anne\Desktop\软工作业\现场编程\学生邮箱.xlsx'

# 读取Excel文件中的数据
df = pd.read_excel(file_path)

def generate(dataframe):
    name_id = dataframe.iloc[1:, 1:2]
    name_id = set(name_id.values.flatten())
    email = dict()
    # 根据姓名提取邮箱
    for name in name_id:
        for index, row in dataframe.iterrows():
            if row[2] == name:
                email[name] = row[2]

    return email

generate(df)