# -'-coding: euc-kr-'-

from Software import *

sw_list = []

data = Software()

data.set_lecture("웹파이썬프로그래밍", "웹파이썬프로그래밍에 대해 배운다.", "1")
sw_list.append(data.lectureList)
data.set_lecture("객체지향프로그래밍", "객체지향프로그래밍에 대해 배운다.", "2")
sw_list.append(data.lectureList)
data.set_lecture("디자인적사고", "디자인적사고에 대해 배운다.", "1")
sw_list.append(data.lectureList)


first_list = []  # 1학년 과목(과목, 학년)이 들어있는 리스트
second_list = []  # 2학년 과목(과목, 학년)이 들어있는 리스트
third_list = []  # 3학년 과목(과목, 학년)이 들어있는 리스트
fourth_list = []  # 4학년 과목(과목, 학년)이 들어있는 리스트
main_list = []  # main 리스트에 1,2,3,4학년 과목 일렬로 쭉 늘어놓기
final_list = []  # 정렬이 된 후 전체 최종 리스트
list1 = []  # 정렬이 된 후 1학년 최종 리스트
list2 = []  # 정렬이 된 후 2학년 최종 리스트
list3 = []  # 정렬이 된 후 3학년 최종 리스트
list4 = []  # 정렬이 된 후 4학년 최종 리스트


fileOut = open("test2.txt", 'w')
for i in range(sw_list.__len__()):
    for j in range(3):
        a = sw_list[i][j] + '\n'
        fileOut.write(a)
fileOut.close()


fileIn = open("test2.txt", 'r')
while True:
    line = fileIn.readline()
    if not line:
        break
    print(line.strip('\n'))
fileIn.close()


a = "프로그래밍"
# for i in data.lectureList:
for i in range(3):
    if a in sw_list[i][1]:
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


# 리스트의 [1] index 의 원소를 기준으로 리스트 정렬하기
for i in range(main_list.__len__()):
    sorted(main_list, key=lambda main: main_list[i][0])

for i in main_list:
    final_list.append(main_list[0])

for i in first_list:
    list1.append(first_list[0])

for i in second_list:
    list2.append(second_list[0])

for i in third_list:
    list3.append(third_list[0])

for i in fourth_list:
    list4.append(fourth_list[0])


print(data.lectureList)
print(sw_list)
print(sw_list[0])
print(first_list)
print(list1)
print(list2)
print(list3)
print(list4)
print(main_list)

