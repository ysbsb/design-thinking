# -*- coding: utf-8 -*-
from ReadData import *

# =====================각 학과 타입 데이터를 저장하는 리스트=========================
sw_list = read_data("Computer.txt")

# test code
print(sw_list)
print(type(sw_list))  # class 'list'
print(sw_list[0])
print(type(sw_list[0]))  # class 'list'
print(sw_list[0][0])
print(type(sw_list[0][0]))  # class 'str'
print(sw_list[0][1])
print(type(sw_list[0][1]))  # class 'str'
print(sw_list[0][2])
print(type(sw_list[0][2]))  # class 'str'
print(sw_list[1])
print(sw_list[2])
print(sw_list.__len__())
print(type('1'))  # class 'str'
print(type("1"))  # class 'str'

a = '1'
b = "1"
if a == b:
    print("ok")


# ===========================학년별 과목  리스트===================================
first_list = []  # 1학년 과목(과목, 학년)이 들어있는 리스트
second_list = []  # 2학년 과목(과목, 학년)이 들어있는 리스트
third_list = []  # 3학년 과목(과목, 학년)이 들어있는 리스트
fourth_list = []  # 4학년 과목(과목, 학년)이 들어있는 리스트
main_list = []  # main 리스트에 1,2,3,4학년 과목 일렬로 쭉 늘어놓기

'''
fileOut = open("Computer.txt", 'w')
for i in range(sw_list.__len__()):
    for j in range(3):
        a = sw_list[i][j] + '\n'
        fileOut.write(a)
fileOut.close()
'''


target = "프로그래밍"
for i in range(sw_list.__len__()):
    if target in sw_list[i][1]:
        if sw_list[i][2] == "1":
            first_list.append([sw_list[i][0], 1])
        elif sw_list[i][2] == "2":
            second_list.append([sw_list[i][0], 2])
        elif sw_list[i][2] == "3":
            third_list.append([sw_list[i][0], 3])
        elif sw_list[i][2] == "4":
            fourth_list.append([sw_list[i][0], 4])
main_list.extend(first_list)
main_list.extend(second_list)
main_list.extend(third_list)
main_list.extend(fourth_list)


'''
test code
======================== 함수처럼 구현하면 list1,2,3,4가 생성이 되지 않는다. =====================
target = "프로그래밍"

def find_keyword(target):
    for i in range(sw_list.__len__()):
        if target in sw_list[i][2]:
            if sw_list[i][2] == "1":
                first_list.append([sw_list[i][0], 1])
            elif sw_list[i][2] == "2":
                second_list.append([sw_list[i][0], 2])
            elif sw_list[i][2] == "3":
                third_list.append([sw_list[i][0], 3])
            elif sw_list[i][2] == "4":
                fourth_list.append([sw_list[i][0], 4])
    main_list.extend(first_list)
    main_list.extend(second_list)
    main_list.extend(third_list)
    main_list.extend(fourth_list)
'''

print(first_list)
print(second_list)
print(third_list)
print(fourth_list)
print(main_list)


'''
test code
# ===========================정렬 후 학년별 과목 리스트===============================
list1 = []  # 정렬이 된 후 1학년 최종 리스트
list2 = []  # 정렬이 된 후 2학년 최종 리스트
list3 = []  # 정렬이 된 후 3학년 최종 리스트
list4 = []  # 정렬이 된 후 4학년 최종 리스트
final_list = []  # 정렬이 된 후 전체 최종 리스트


sorted(main_list, key=lambda x: x[1])


for i in range(main_list.__len__()):
    final_list.append(main_list[i])

for i in range(first_list.__len__()):
    list1.append(first_list[i])

for i in range(second_list.__len__()):
    list2.append(second_list[i])

for i in range(third_list.__len__()):
    list3.append(third_list[i])

for i in range(fourth_list.__len__()):
    list4.append(fourth_list[i])


print(list1)
print(list2)
print(list3)
print(list4)
print(final_list)
'''

