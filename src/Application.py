from Embedded import *


class Application:
    """Application 클래스

    """

    def __init__(self):
        """기본 생성자

        job_data : 사용자에게 받을 직업의 이름
        dep_data : 사용자에게 받을 학과 이름 (department)
        """
        self.job_data = ""
        self.dep_data = ""

    def command(self):
        """사용자에게 원하는 직업과, 학과를 묻는 명령창이다.

        :return: None
        """
        print("\n1) 임베디드소프트웨어전문가")
        self.job_data = input("원하는 직업을 입력하세요: ")
        print("\n1) 소프트웨어융합학과, 2) 컴퓨터공학과 3) 전자공학과")
        self.dep_data = input("학과를 입력하세요.: ")

    def display_data(self):
        """사용자에게 입력 받은 직업과 학과에 맞는 교과목 정보를 알려준다.

        example)
        소프트웨어융합학과의 한 학생이 '임베디드소프트웨어전문가' 가 되고 싶어서
        '임베디드소프트웨어전문가'가 되려면 어떤 수업을 들어야 하는지 찾아보려고 한다.

        command 에 임베디드소프트웨어를 입력하고,
        학과에는 '소프트웨어융합학과'를 입력한다.
        (구현한 모델에는 번호 입력으로 되어있다.)

        임베디소프트웨어에 해당하는 직업에 필요한 능력 키워드와
        소프트웨어융합학과 교과목에서 배우는 내용 키워드를 비교하여
        학생이 들으면 좋은 과목들을 추천해준다.

        :return: None
        """
        if self.job_data == '1':
            if self.dep_data == '1':
                for i in range(univ.sw_main_list.__len__()):
                    print(univ.sw_main_list[i][0], ":", univ.sw_main_list[i][1])
            elif self.dep_data == '2':
                for i in range(univ.cs_main_list.__len__()):
                    print(univ.cs_main_list[i][0], ":", univ.cs_main_list[i][1])
            elif self.dep_data == '3':
                for i in range(univ.ee_main_list.__len__()):
                    print(univ.ee_main_list[i][0], ":", univ.ee_main_list[i][1])

    def write_data(self):
        if self.dep_data == '1':
            file_out = open("SW_data.txt", 'w', encoding='utf-8')
            a = ""
            for i in range(univ.sw_main_list.__len__()):
                a = univ.sw_main_list[i][0] + ":" + univ.sw_main_list[i][1] + "\n"
                file_out.write(a)
            file_out.close()

        elif self.dep_data == '2':
            file_out = open("CS_data.txt", 'w', encoding='utf-8')
            for i in range(univ.cs_main_list.__len__()):
                a = univ.cs_main_list[i][0] + ":" + univ.cs_main_list[i][1] + "\n"
                file_out.write(a)
            file_out.close()

        elif self.dep_data == '3':
            file_out = open("EE_data.txt", 'w', encoding='utf-8')
            for i in range(univ.ee_main_list.__len__()):
                a = univ.ee_main_list[i][0] + ":" + univ.ee_main_list[i][1] + "\n"
                file_out.write(a)
            file_out.close()


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

