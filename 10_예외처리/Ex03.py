'''
Created on 2024. 8. 8.

@author: user
'''

while True :
    print('---Menu 선택---')
    print('1.전체 조회')
    print('2.추가')
    print('3.수정')
    print('4.삭제')
    print('0.종료')
    menu = int(input('번호 선택:'))
    
    if menu == 1:
        print('1.전체 조회')
        print('제목\t가격')
        try:
            br = open('File.txt','r',encoding='UTF-8')
        except FileNotFoundError :
            bw = open('File.txt','w',encoding='UTF-8')
            bw.close()
            br = open('File.txt','r',encoding='UTF-8')
        
        for line in br: 
            print(line,end='')
        
    elif menu == 2:
        print('2.추가')
        while True :
            try :
                title = input('제목:')
                if len(title)>5 :
                    raise ValueError
                else :
                    break
            except ValueError:
                print('제목 5글자 이하로 입력하세요')
                
        
        while True :
            try :
                price = int(input('가격:'))
               
            except ValueError:
                print('가격은 숫자로 입력하세요')
            else :
                break
                    
        bw = open('File.txt','a',encoding='UTF-8') 
        bw.write(title+','+str(price)+'\n')
        bw.close()
        
    elif menu == 3:
        pass
    elif menu == 4:
        pass
    elif menu == 0:
        break
    else :
        print("0~4만 가능")

print('프로그램을 종료합니다.')

#
# ----- Menu Select -----
# 1. 전체 조회
# 2. 추가
# 3. 수정
# 4. 삭제
# 0. 종료
# 번호 선택: 1
# 1. 전체조회
# 제목    가격
# ----- Menu Select -----
# 1. 전체 조회
# 2. 추가
# 3. 수정
# 4. 삭제
# 0. 종료
# 번호 선택: 2
# 2. 추가
# 제목:자바
# 가격:300
# ----- Menu Select -----
# 1. 전체 조회
# 2. 추가
# 3. 수정
# 4. 삭제
# 0. 종료
# 번호 선택: 1
# 1. 전체조회
# 제목    가격
# bookList: ['자바,300']
# 자바      300
# ----- Menu Select -----
# 1. 전체 조회
# 2. 추가
# 3. 수정
# 4. 삭제
# 0. 종료
# 번호 선택: 2
# 2. 추가
# 제목:JSP
# 가격:400
# ----- Menu Select -----
# 1. 전체 조회
# 2. 추가
# 3. 수정
# 4. 삭제
# 0. 종료
# 번호 선택: 1
# 1. 전체조회
# 제목    가격
# bookList: ['자바,300']
# bookList: ['자바,300', 'JSP,400']
# 자바      300
# JSP      400
# ----- Menu Select -----
# 1. 전체 조회
# 2. 추가
# 3. 수정
# 4. 삭제
# 0. 종료
# 번호 선택: 2
# 2. 추가
# 제목:adfdfsfds
# 제목 5글자 이상입력됨
# 제목:abcd
# 가격:sdsdfs
# 가격은 숫자로 입력하세요
# 가격:sdsf
# 가격은 숫자로 입력하세요
# 가격:sdfsf
# 가격은 숫자로 입력하세요
# 가격:fsd
# 가격은 숫자로 입력하세요
# 가격:500
# ----- Menu Select -----
# 1. 전체 조회
# 2. 추가
# 3. 수정
# 4. 삭제
# 0. 종료
# 번호 선택: 1
# 1. 전체조회
# 제목    가격
# bookList: ['자바,300']
# bookList: ['자바,300', 'JSP,400']
# bookList: ['자바,300', 'JSP,400', 'abcd,500']
# 자바      300
# JSP      400
# abcd      500
# ----- Menu Select -----
# 1. 전체 조회
# 2. 추가
# 3. 수정
# 4. 삭제
# 0. 종료
# 번호 선택: 3
# 3. 수정
# 제목:adfsfdsf
# 제목 5글자 이상입력됨
# 제목:JSP
# 수정할 가격:700
# d: {'자바': '300', 'JSP': '400', 'abcd': '500'}
# 찾음
# ----- Menu Select -----
# 1. 전체 조회
# 2. 추가
# 3. 수정
# 4. 삭제
# 0. 종료
# 번호 선택: 1
# 1. 전체조회
# 제목    가격
# bookList: ['자바,300']
# bookList: ['자바,300', 'JSP,700']
# bookList: ['자바,300', 'JSP,700', 'abcd,500']
# 자바      300
# JSP      700
# abcd      500
# ----- Menu Select -----
# 1. 전체 조회
# 2. 추가
# 3. 수정
# 4. 삭제
# 0. 종료
# 번호 선택: 3
# 3. 수정
# 제목:스프링
# 수정할 가격:3232
# d: {'자바': '300', 'JSP': '700', 'abcd': '500'}
# 못찾음
# ----- Menu Select -----
# 1. 전체 조회
# 2. 추가
# 3. 수정
# 4. 삭제
# 0. 종료
# 번호 선택: 4
# 4. 삭제
# 삭제할 제목:스프링
# d: {'자바': '300', 'JSP': '700', 'abcd': '500'}
# 못찾음
# ----- Menu Select -----
# 1. 전체 조회
# 2. 추가
# 3. 수정
# 4. 삭제
# 0. 종료
# 번호 선택: 4
# 4. 삭제
# 삭제할 제목:JSP
# d: {'자바': '300', 'JSP': '700', 'abcd': '500'}
# 찾음
# ----- Menu Select -----
# 1. 전체 조회
# 2. 추가
# 3. 수정
# 4. 삭제
# 0. 종료
# 번호 선택: 1
# 1. 전체조회
# 제목    가격
# bookList: ['자바,300']
# bookList: ['자바,300', 'abcd,500']
# 자바      300
# abcd      500
# ----- Menu Select -----
# 1. 전체 조회
# 2. 추가
# 3. 수정
# 4. 삭제
# 0. 종료
# 번호 선택: 7
# 잘못 입력
# ----- Menu Select -----
# 1. 전체 조회
# 2. 추가
# 3. 수정
# 4. 삭제
# 0. 종료
# 번호 선택: 0
# 0. 종료
# --------------------------------
# File.txt에 기록
# 자바,300
# JSP,500








