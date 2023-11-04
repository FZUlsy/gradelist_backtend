import openpyxl
import openpyxl

# 1. 读取Excel文件
def read_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    worksheet = workbook.active

    # 创建一个字典来存储学生成绩，其中键为学号，值为学生信息列表
    scores = {}

    # 假设学号在B列，姓名在C列，课程名称在D列，百分成绩在F列，从第2行开始
    for row in worksheet.iter_rows(min_row=3, values_only=True):
        _, student_id, student_name, course_name, _, percentage_score, _, _, _ = row

        if student_name not in scores:
            scores[student_name] = {'id': student_id, 'scores': []}

        scores[student_name]['scores'].append((course_name, percentage_score))

    return scores

# 2. 生成成绩单文本
def generate_report(scores, student_name):
    report = ""
    student_info = scores[student_name]
    student_id = student_info['id']
    student_scores = student_info['scores']
    
    report += f"亲爱的{student_name}同学:\n\n"
    report += "祝贺您顺利完成本学期的学习！教务处在此向您发送最新的成绩单。\n\n"

    for course_name, percentage_score in student_scores:
        report += f"{course_name}： {percentage_score} "

    report += "\n\n"
    report += "希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。如果您在某些科目上没有达到预期的成绩，不要灰心，这也是学习过程中的一部分。我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。\n\n"
    report += "再次恭喜您，祝您学习进步、事业成功！\n\n"
    report += "教务处\n\n\n"

    return report

# 3. 将成绩单文本保存到txt文件
def save_to_txt(report, output_file):
    with open(output_file, 'w', encoding='utf-8') as txt_file:
        txt_file.write(report)

if __name__ == "__main__":
    # excel_file的值为需要导入的excel文件的路径
    excel_file = 'C:\\Users\\hikaru\\Desktop\\成绩表.xlsx'


    # 读取Excel数据
    scores = read_excel(excel_file)
    # outputfile[]的值为需要生成的txt文件的保存路径
    # 生成并保存成绩单1（张三）
    report1 = generate_report(scores, '张三')
    output_file1 = 'C:\\Users\\hikaru\\Desktop\\成绩单1.txt'
    save_to_txt(report1, output_file1)
    # outputfile[]的值为需要生成的txt文件的保存路径
    # 生成并保存成绩单2（李四）
    report2 = generate_report(scores, '李四')
    output_file2 = 'C:\\Users\\hikaru\\Desktop\\成绩单2.txt'
    save_to_txt(report2, output_file2)
    # outputfile[]的值为需要生成的txt文件的保存路径
    # 生成并保存成绩单3（王五）
    report3 = generate_report(scores, '王五')
    output_file3 = 'C:\\Users\\hikaru\\Desktop\\成绩单3.txt'
    save_to_txt(report3, output_file3)