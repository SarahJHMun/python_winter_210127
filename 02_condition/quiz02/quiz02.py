# 1. 
score1, score2 = input("두 점수를 입력하세요: ").split()
score1 = int(score1)
score2 = int(score2)

if score1 >= 70 and score2 >= 70:
    print("합격입니다.")
    
# 2.
# 공배수 구하기(2와 3의 공배수인지)
n = int(input("수를 입력하세요: "))

if n % 2 == 0 and n % 3 == 0:
    print("%d는 2와 3의 공배수 입니다." % n)
    
    
# 3
n = int(input("1~10 사이의 수를 입력하세요: "))

if n < 1 or n > 10:
    print("잘못 입력하셨습니다.")
