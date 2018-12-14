# -*- coding: utf-8 -*-

from ReadSWData import *
from ReadCSData import *
from ReadEEData import *


class University:
    """
    ==================================================================================

                             소프트웨어융합학과, 컴퓨터공학과, 전자공학과의
                                    모든 교과목 정보를 불러오고
                        교과목 정보가 저장된 리스트를 가진 University 클래스

    ==================================================================================
    """

    def __init__(self):
        """기본 생성자

        파일 read data 함수로 텍스트 파일에서 읽은 모든 학과 정보를 리스트에 저장한다.
        각 교과목 학년별 리스트는 초기화 리스트 이다.

        """
        # =====================각 학과 타입 데이터를 불러온다. =========================
        self.sw_list = read_sw_data("Software.txt")
        self.cs_list = read_cs_data("Computer.txt")
        self.ee_list = read_ee_data("Electronic.txt")

        # ===========================소프트웨어융합학과 학년별 과목  리스트===================================
        self.sw_first_list = []  # 키워드로 선별된 1학년 과목(과목, 학년)이 들어있는 리스트
        self.sw_second_list = []  # 키워드로 선별된 2학년 과목(과목, 학년)이 들어있는 리스트
        self.sw_third_list = []  # 키워드로 선별된 3학년 과목(과목, 학년)이 들어있는 리스트
        self.sw_fourth_list = []  # 키워드로 선별된 4학년 과목(과목, 학년)이 들어있는 리스트
        self.sw_main_list = []  # 키워드로 선별된 main 리스트에 1,2,3,4학년 과목 일렬로 쭉 늘어놓기

        # ===========================컴퓨터공학과 학년별 과목  리스트===================================
        self.cs_first_list = []  # 키워드로 선별된 1학년 과목(과목, 학년)이 들어있는 리스트
        self.cs_second_list = []  # 키워드로 선별된 2학년 과목(과목, 학년)이 들어있는 리스트
        self.cs_third_list = []  # 3학년 과목(과목, 학년)이 들어있는 리스트
        self.cs_fourth_list = []  # 키워드로 선별된 4학년 과목(과목, 학년)이 들어있는 리스트
        self.cs_main_list = []  # 키워드로 선별된 main 리스트에 1,2,3,4학년 과목 일렬로 쭉 늘어놓기

        # ===========================전자공학과 학년별 과목  리스트===================================
        self.ee_first_list = []  # 키워드로 선별된 1학년 과목(과목, 학년)이 들어있는 리스트
        self.ee_second_list = []  # 키워드로 선별된 2학년 과목(과목, 학년)이 들어있는 리스트
        self.ee_third_list = []  # 키워드로 선별된 3학년 과목(과목, 학년)이 들어있는 리스트
        self.ee_fourth_list = []  # 키워드로 선별된 4학년 과목(과목, 학년)이 들어있는 리스트
        self.ee_main_list = []  # 키워드로 선별된 main 리스트에 1,2,3,4학년 과목 일렬로 쭉 늘어놓기


'''
# test code
univ = University()
print("sw")
print(univ.sw_list)
print(univ.sw_list.__len__())
print("cs")
print(univ.cs_list)
print("ee")
print(univ.ee_list)
'''