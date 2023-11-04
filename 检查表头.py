import openpyxl

# 打开Excel文件
try:
    workbook = openpyxl.load_workbook('ta.xlsx')  # 加载Excel文件
except FileNotFoundError:
    print("文件不存在或路径错误，请确认文件路径是否正确。")

# 选择第一个工作表
sheet = workbook.active  # 获取当前活动的工作表

# 检查表头是否符合要求
header = ['选课时间', '学号', '姓名', '课程名称', '学分', '百分成绩', '五分成绩', '考试类型', '选修类型']
first_row = [cell.value for cell in sheet[2]]  # 获取第一行的内容
if first_row != header:
    print("表头不符合要求，请检查Excel文件的表头内容。")
