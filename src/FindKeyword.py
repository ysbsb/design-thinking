# -*- coding: utf-8 -*-

from University import *

"""
======================================================================================
                         직업의 키워드와 일치하는 과목 리스트를 만든다.
======================================================================================
"""

univ = University()     # univ : University 클래스 타입의 data

# test code
# print(univ.sw_list)
# print(univ.sw_list.__len__())


def find_in_sw(keyword):
    """소프트웨어융합학과 교과목 리스트의 수업 내용에서 "keyword"를 찾으면 학년별 리스트에 저장한다.

    example)
    입력 파라미터 keyword = "프로그래밍" 이라고 하자.
    sw_list = [["웹\파이선프로그래밍", "웹\파이선프로그래밍에 대해서 배운다.", "1"], ["a","a","a"], ...,["z","z","z"]]
    sw_list[0][1] 의 내용에 "프로그래밍" 이 있으므로
    sw_first_list 에 ["웹\파이선프로그래밍", "1"] 를 추가한다.

    :param keyword: 내가 찾고 싶은 키워드 이다. ex) 프로그래밍
    :return: None
    """

    for i in range(univ.sw_list.__len__()):
        if keyword in univ.sw_list[i][1]:
            if univ.sw_list[i][2] == "1":
                if [univ.sw_list[i][0], "1"] in univ.sw_first_list:
                    continue
                else:
                    univ.sw_first_list.append([univ.sw_list[i][0], "1"])
            elif univ.sw_list[i][2] == "2":
                if [univ.sw_list[i][0], "2"] in univ.sw_second_list:
                    return False
                else:
                    univ.sw_second_list.append([univ.sw_list[i][0], "2"])
            elif univ.sw_list[i][2] == "3":
                if [univ.sw_list[i][0], "3"] in univ.sw_third_list:
                    return False
                else:
                    univ.sw_third_list.append([univ.sw_list[i][0], "3"])
            elif univ.sw_list[i][2] == "4":
                if [univ.sw_list[i][0], "4"] in univ.sw_fourth_list:
                    return False
                else:
                    univ.sw_fourth_list.append([univ.sw_list[i][0], "4"])


def add_to_sw_main_list():
    """sw_main_list 에 키워드로 선별된 각 학년별 과목 리스트를 뒤에 덧붙여주는 함수

    :return: None
    """
    univ.sw_main_list.extend(univ.sw_first_list)
    univ.sw_main_list.extend(univ.sw_second_list)
    univ.sw_main_list.extend(univ.sw_third_list)
    univ.sw_main_list.extend(univ.sw_fourth_list)


def find_in_cs(keyword):
    """컴퓨터공학과 교과목 리스트의 수업 내용에서 "keyword"를 찾으면 학년별 리스트에 저장한다.

    example)
    입력 파라미터 keyword = "구조" 이라고 하자.
    sw_list = [["자료구조", "자료구조.", "2"], ["컴퓨터구조", "컴퓨터구조.", "2"], ["a","a","a"], ...,["z","z","z"]]
    sw_list[0][1] 와  sw_list[0][2] 의 내용에 "구조" 가 있으므로
    sw_second_list 에
    ["자료구조", "2"]와 ["컴퓨터구조", "2"] 를 추가한다.

    :param keyword: 내가 찾고 싶은 키워드 이다. ex) 구조
    :return: None
    """

    for i in range(univ.cs_list.__len__()):
        if keyword in univ.cs_list[i][1]:
            if univ.cs_list[i][2] == "1":
                if [univ.cs_list[i][0], "1"] in univ.cs_first_list:
                    return 0
                else:
                    univ.cs_first_list.append([univ.cs_list[i][0], "1"])
            elif univ.cs_list[i][2] == "2":
                if [univ.cs_list[i][0], "2"] in univ.cs_second_list:
                    return 0
                else:
                    univ.cs_second_list.append([univ.cs_list[i][0], "2"])
            elif univ.cs_list[i][2] == "3":
                if [univ.cs_list[i][0], "3"] in univ.cs_third_list:
                    return 0
                else:
                    univ.cs_third_list.append([univ.cs_list[i][0], "3"])
            elif univ.cs_list[i][2] == "4":
                if [univ.cs_list[i][0], "4"] in univ.cs_fourth_list:
                    return 0
                else:
                    univ.cs_fourth_list.append([univ.cs_list[i][0], "4"])


def add_to_cs_main_list():
    """cs_main_list 에 키워드로 선별된 각 학년별 과목 리스트를 뒤에 덧붙여주는 함수

    :return: None
    """
    univ.cs_main_list.extend(univ.cs_first_list)
    univ.cs_main_list.extend(univ.cs_second_list)
    univ.cs_main_list.extend(univ.cs_third_list)
    univ.cs_main_list.extend(univ.cs_fourth_list)


def find_in_ee(keyword):
    """전자공학과 교과목 리스트의 수업 내용에서 "keyword"를 찾으면 학년별 리스트에 저장한다.

    example)
    입력 파라미터 keyword = "프로그래밍" 이라고 하자.
    sw_list = [["웹\파이선프로그래밍", "웹\파이선프로그래밍에 대해서 배운다.", "1"], ["a","a","a"], ...,["z","z","z"]]
    sw_list[0][1] 의 내용에 "프로그래밍" 이 있으므로
    sw_first_list 에 ["웹\파이선프로그래밍", "웹\파이선프로그래밍에 대해서 배운다.", "1"] 를 추가한다.

    :param keyword: 내가 찾고 싶은 키워드 이다. ex) 프로그래밍
    :return: None
    """

    for i in range(univ.ee_list.__len__()):
        if keyword in univ.ee_list[i][1]:
            if univ.ee_list[i][2] == "1":
                if [univ.ee_list[i][0], "1"] in univ.ee_first_list:
                    continue
                else:
                    univ.ee_first_list.append([univ.ee_list[i][0], "1"])
            elif univ.ee_list[i][2] == "2":
                if [univ.ee_list[i][0], "2"] in univ.ee_second_list:
                    return False
                else:
                    univ.ee_second_list.append([univ.ee_list[i][0], "2"])
            elif univ.ee_list[i][2] == "3":
                if [univ.ee_list[i][0], "3"] in univ.ee_third_list:
                    return False
                else:
                    univ.ee_third_list.append([univ.ee_list[i][0], "3"])
            elif univ.ee_list[i][2] == "4":
                if [univ.ee_list[i][0], "4"] in univ.ee_fourth_list:
                    return False
                else:
                    univ.ee_fourth_list.append([univ.ee_list[i][0], "4"])


def add_to_ee_main_list():
    """ee_main_list 에 키워드로 선별된 각 학년별 과목 리스트를 뒤에 덧붙여주는 함수

    :return: None
    """
    univ.ee_main_list.extend(univ.ee_first_list)
    univ.ee_main_list.extend(univ.ee_second_list)
    univ.ee_main_list.extend(univ.ee_third_list)
    univ.ee_main_list.extend(univ.ee_fourth_list)


'''
test code
find_in_sw("소프트웨어")
print("소프트웨어융합학과")
print("fist list")
print(univ.sw_first_list)
print("second list")
print(univ.sw_second_list)
print("third list")
print(univ.sw_third_list)
print("fourth list")
print(univ.sw_fourth_list)
print("main list")
print(univ.sw_main_list)

find_in_cs("프로그래밍")
print("컴퓨터공학과")
print("fist list")
print(univ.sw_first_list)
print("second list")
print(univ.sw_second_list)
print("third list")
print(univ.sw_third_list)
print("fourth list")
print(univ.sw_fourth_list)
print("main list")
print(univ.sw_main_list)

find_in_ee("회로")
print("전자공학과")
print("fist list")
print(univ.sw_first_list)
print("second list")
print(univ.sw_second_list)
print("third list")
print(univ.sw_third_list)
print("fourth list")
print(univ.sw_fourth_list)
print("main list")
print(univ.sw_main_list)
'''
