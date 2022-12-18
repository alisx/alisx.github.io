
checkfile = open("2022-06-20.txt", "r", encoding='utf-8')

late_count = 0 # 迟到人数统计
absence_count = 0 # 缺勤人数统计

lates = [] # 迟到员工编号
absences = [] # 缺勤员工编号

for l in checkfile:
    info = l.split(',')
    if info[1] == '迟到':
        late_count += 1 # 累加迟到人数
        lates.append(info[0]) # 记录迟到员工号
    elif info[1] == '缺勤':
        absence_count += 1 # 累加缺勤人数
        absences.append(info[0]) # 记录缺勤员工号
            
print("迟到人数：", late_count)
print("迟到员工号：", lates)

print("缺勤人数：", absence_count)
print("缺勤员工号：", absences)

checkfile.close() # 记得关闭哦
