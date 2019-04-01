# -*- coding: utf-8 -*-


class Computer:
    """
    ==================================================================================
                                컴퓨터공학과 수업 정보 클래스
    ==================================================================================
    """

    def __init__(self):
        """기본 생성자

        """
        self.className = ""     # 수업 이름
        self.summary = ""       # 수업 내용 요약
        self.grade = ""         # 수강 학년
        self.lectureList = []   # 교과목 정보 리스트. 한 수업에 대한 이름, 내용, 학년 정보가 들어있다.
        self.cs_list = []       # 컴퓨터공학과의 전체 교과목 정보가 들어있는 리스트. 여러개의 교과목 리스트로 이루어져 있다.

    def set_lecture(self, lecture, contents, lec_grade):
        """교과목 정보를 저장하고, 학과 수업 리스트에 과목 정보를 추가하는 함수

        :param lecture: 수업 이름
        :param contents: 수업 요약 정보
        :param lec_grade: 수강 학년
        :return:
        """
        self.className = lecture
        self.summary = contents
        self.grade = lec_grade
        self.lectureList = [self.className, self.summary, self.grade]
        self.cs_list.append([self.className, self.summary, self.grade])

    def make_list_empty(self):
        """교과목 리스트를 비우는 함수

        :return: None
        """
        self.lectureList = []

