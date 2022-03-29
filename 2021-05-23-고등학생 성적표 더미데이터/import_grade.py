#!/bin/python3
# pip install pandas
# pip install openpyxl
# pip install faker

import pandas
import pymysql
import random

from faker import Faker
fake = Faker('ko_KR')

## MySQL Connection 연결
conn = pymysql.connect(host='192.168.10.130', user='root', password='asdf1234', db='data',
                    charset='utf8')

## Connection 으로부터 Cursor 생성
curs = conn.cursor()

def import_school(excel_path, sheet_name):
    df = pandas.read_excel(excel_path, sheet_name, engine = 'openpyxl')
    for index, row in df.iterrows():
        sql = "insert into tb_school (name, category) values ('{}', '고등학교')".format(str(row.이름))
        curs.execute(sql)
        rows = curs.fetchall()
        conn.commit()

def import_affiliation():
    for x in range(1,327):
        sql = "insert into tb_affiliation (area_id, school_id) values (1, {})".format(x)
        curs.execute(sql)
        rows = curs.fetchall()
        conn.commit()

def import_student():
    sql = "select id from tb_school"
    curs.execute(sql)
    rows = curs.fetchall()
    for cnt_school in rows:
        for year in range(2010, 2021):
            people = random.randrange(1000, 1201)
            for cnt_student in range(people):
                name = fake.name()
                sql = "insert into tb_student (name, entrance, school_id) values ('{}',{}, {})".format(str(name), int(year), int(cnt_school[0]))
                #print(sql)
                curs.execute(sql)
                rows = curs.fetchall()
                conn.commit()

def import_grade():
    sql = "select id,entrance from tb_student"
    curs.execute(sql)
    rows = curs.fetchall()
    list_subject = ['국어', '수학', '영어', '과학', '사회', '체육']

    for cnt_student in rows:
        for cnt_year in range(int(cnt_student[1]), int(cnt_student[1]+3)):

            #print("{}년도".format(cnt_year))
            for cnt_semester in range(1,3):
                #print("{}학기".format(cnt_semester))
                for cnt_subject in range(len(list_subject)):
                    #print(list_subject[cnt_subject])
                    sql = "insert into tb_grade (student_id, year, semester, subject, grade) \
                            values ({}, {}, {} ,'{}' ,{})".format(int(cnt_student[0]), int(cnt_year), int(cnt_semester), list_subject[cnt_subject] , random.randrange(0, 101) )
                    curs.execute(sql)
                    rows = curs.fetchall()
                    conn.commit()

if __name__ == '__main__':

    excel_path = "high.xlsx"
    sheet_name = "Sheet1"	    
	
	#import_school(excel_path, sheet_name)
	#import_student()
	#import_grade()
	

    while 1:
        print('############ Excel Import Manager ##########')
        print('#### tb_area, tb_school, tb_affiliation 테이블이 있는지 확인해주세요')
        print('1. 학교 데이터를 엑셀에서 불러와 추가합니다')
        print('2. 학생 데이터를 faker로 생성하여 추가합니다.')
        print('3. 성적 데이터를 faker로 생성하여 추가합니다.')
        print('4. 종료')
        menu = int(input('메뉴를 선택하세요 : '))
        excel_path = "C:\\Users\\unknown\\Documents\\git_test\\sql_test\\sql_test\\2021-05-23-고등학생 성적표 더미데이터\\high.xlsx"
        sheet_name = "Sheet1"

        if menu == 1:
            import_school(excel_path, sheet_name)
        elif menu == 2:
            import_student()
        elif menu == 3:
            import_grade()
        elif menu == 4:
            #conn.close()
            break
        else :
            print("없는 메뉴입니다. 다시 입력해주세요.")    
