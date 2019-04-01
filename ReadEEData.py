# -*- coding: utf-8 -*-

from Electronic import *


"""
======================================================================================
                        파일로부터 전자공학과 교과목 정보를 읽는다.  
======================================================================================
"""

ee_data = Electronic()   # ee_data : Electronic 클래스 타입의 data


def read_ee_data(filename):
    """텍스트 파일에서 교과목 정보를 불러와 리스트에 저장하는 함수

    :param filename: 텍스트 파일 이름
    :return: sw_data.sw_list    소프트웨어융합학과의 전체 교과목 정보가 들어있는 리스트
    """
    i = 0   # 반복 표시 인덱스 : 파일에서 3줄을 읽을 때 마다 한 과목의 정보이다.
    # 해당 디렉토리에 이름이 'filename'인 파일을 찾고 파일을 연다.
    # 이 때 한글을 읽기 위해서 encoding 은 'utf-8'로 한다.
    file_in = open(filename, 'r', encoding='utf-8')
    while True:
        line = file_in.readline()   # 파일에서 한 줄씩 읽는다.
        if not line:
            break
        a = line.strip('\n')    # '\n'도 한 줄씩 읽힐 수 있으므로 제거한다.

        if i == 2:
            ee_data.lectureList.append(a)   # 수강 학년 교과목 리스트에 추가하기
            ee_data.ee_list.append(ee_data.lectureList)     # 교과목 리스트를 학과 수업 리스트에 추가하기
            ee_data.make_list_empty()   # 다른 교과목을 받기 위하여, 기존 교과목 리스트를 비우기.
            i = 0
        elif i == 1:
            ee_data.lectureList.append(a)   # 수업 내용 교과목 리스트에 추가하기
            i = i + 1
        elif i == 0:
            ee_data.lectureList.append(a)   # 수업 이름 교과목 리스트에 추가하기
            i = i + 1
    file_in.close()

    # test code
    # print(ee_data.ee_list)

    return ee_data.ee_list       # 전자공학과 학과 수업 리스트 리턴


'''
# test code
print("ee")
print(read_ee_data("Electronic.txt"))


ee_list = read_ee_data("Electronic.txt")

fileOut = open("Electronic.txt", 'w')
for i in range(ee_list.__len__()):
    for j in range(3):
        a = ee_list[i][j] + '\n'
        fileOut.write(a)
fileOut.close()
'''
