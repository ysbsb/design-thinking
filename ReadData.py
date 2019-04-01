# -*- coding: utf-8 -*-
from Software import *
from Computer import *
from Electronic import *

"""
======================================================================================
                            파일로부터 교과목 정보를 읽는다.  
======================================================================================
"""

sw_data = Software()
cs_data = Computer()
ee_data = Electronic()


def read_data(filename):
    """텍스트 파일에서 교과목 정보를 불러오는 함수

    :param filename: 텍스트 파일 이름
    :return: sw_data.sw_list    소프트웨어융합학과의 전체 교과목 정보가 들어있는 리스트
    """
    i = 0
    file_in = open(filename, 'r')
    while True:
        line = file_in.readline()
        if not line:
            break
        a = line.strip('\n')

        if i == 2:
            sw_data.lectureList.append(a)
            sw_data.sw_list.append(sw_data.lectureList)
            sw_data.make_list_empty()
            i = 0
        elif i == 1:
            sw_data.lectureList.append(a)
            i = i + 1
        elif i == 0:
            sw_data.lectureList.append(a)
            i = i + 1
    file_in.close()

    # test code
    # print(sw_data.sw_list)

    return sw_data.sw_list

# test code
# print(read_data("Computer.txt"))
