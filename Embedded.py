# -*- coding: utf-8 -*-

from FindKeyword import *


def read_embedded_data(filename):
    """텍스트 파일에서 직업 키워드 정보를 불러오는 함수

    :param filename: 텍스트 파일 이름
    :return: sw_data.sw_list    소프트웨어융합학과의 전체 교과목 정보가 들어있는 리스트
    """
    file_in = open(filename, 'r', encoding='utf-8')
    while True:
        line = file_in.readline()
        if not line:
            break
        a = line.strip('\n')
        find_in_sw("a")
        find_in_cs("a")
        find_in_ee("a")

    file_in.close()


# "Embedded.txt"라는 이름의 파일을 읽어, 임베디드소프트웨어전문가 키워드와 유사한 교과목 키워드를 찾는다.
read_embedded_data("Embedded.txt")

add_to_sw_main_list()   # sw_main_list 에 소프트웨어융합학과 수업 중 Embedded 키워드와 비교하여 유사한 과목을 넣는다.
add_to_cs_main_list()   # cs_main_list 에 컴퓨터공학과 수업 중 Embedded 키워드와 비교하여 유사한 과목을 넣는다.
add_to_ee_main_list()   # ee_main_list 에 전자공학과 수업 중 Embedded 키워드와 비교하여 유사한 과목을 넣는다.


'''
# test code
# find_in_sw("소프트웨어")
print("소프트웨어융합학과")
print("fist list")
print(univ.sw_first_list)
print(univ.sw_first_list.__len__())
print("\nsecond list")
print(univ.sw_second_list)
print(univ.sw_second_list.__len__())
print("\nthird list")
print(univ.sw_third_list)
print(univ.sw_third_list.__len__())
print("\nfourth list")
print(univ.sw_fourth_list)
print(univ.sw_fourth_list.__len__())
print("\nmain list")
print(univ.sw_main_list)
print(univ.sw_main_list.__len__())


# find_in_cs("프로그래밍")
print("컴퓨터공학과")
print("fist list")
print(univ.cs_first_list)
print(univ.cs_first_list.__len__())
print("\nsecond list")
print(univ.cs_second_list)
print(univ.cs_second_list.__len__())
print("\nthird list")
print(univ.cs_third_list)
print(univ.cs_third_list.__len__())
print("\nfourth list")
print(univ.cs_fourth_list)
print(univ.cs_fourth_list.__len__())
print("\nmain list")
print(univ.cs_main_list)
print(univ.cs_main_list.__len__())


# find_in_ee("회로")
print("전자공학과")
print("fist list")
print(univ.ee_first_list)
print(univ.ee_first_list.__len__())
print("\nsecond list")
print(univ.ee_second_list)
print(univ.ee_second_list.__len__())
print("\nthird list")
print(univ.ee_third_list)
print(univ.ee_third_list.__len__())
print("\nfourth list")
print(univ.ee_fourth_list)
print(univ.ee_fourth_list.__len__())
print("\nmain list\n\n")
print(univ.ee_main_list)
print(univ.ee_main_list.__len__())
'''

