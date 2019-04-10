# else는 예외처리 용도로 씀.
# && = and, || = or 랑 같은 의미.
# if a == 1 or b == 3:는 if a == 1 || b == 3:이랑 같음.
# 
"""
input 받기.
a: 90점 이상.
b: ......
예외처리
"""
#1: 점수를 입력받고 그 점수가 몇 등급(A~F)인지 알려준다. 이 과정을 특정 조건을 만족하기 전까지 무한히 반복하도록 코드 작성하기.
flag = 1
while flag == 1:
    score = int(input("Your score: "))
    if score >= 90 and score <= 100:
        print("Your grade: A")

    elif score >= 80 and score < 90:
        print("Your grade: B")

    elif score >= 70 and score < 80:
        print("Your grade: C")

    elif score >= 60 and score < 70:
        print("Your grade: D")

    elif score < 60 and score >= 0:
        print("Your grade: F")

    else: # error handling = 예외처리. try에 해당하는 조건에 해당하면 except에 있는 명령들을 실행한다.
        try:
        except: "error name"
            print("Input type error.")

    ind = input("Keep going? (y/n): ")
    if ind == "n":
        flag = 0
    elif ind == "y":
        flag = 1
    else:
        
        print("Input error")
# 숫자 야구 만들기
"""
1. 랜덤(0~9 사이)으로 서로 다른 값 3개 받기.
2. 자릿수 = 숫자: 스트라이크, 자릿수 != 숫자 볼
3. 3스트라이크 = 아웃
ps. 중복되는 숫자를 주는 것도, 입력받는 것도 안 됨.
"""