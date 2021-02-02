# 1. 정수를 입력 받고 음수인지 양수인지 출력하세요.
num = int(input("정수를 입력하세요:"))

if num < 0:
    print("음수")
else:
    print("양수")

# 2. 점수를 입력 받고 90 점이상이면 A , 80점 이상 B, 70점 이상 C, 60점 이상 D, 그외 F 를 출력하세요
score = int(input("점수를 입력하세요:"))
if score >= 90:
    print("A")
elif score >= 80:  # 80 ~ 89
    print("B")
elif score >= 70:  # 70 ~ 79
    print("C")
elif score >= 60:  # 60 ~ 69
    print("D")
else:              # ~59
    print("F")

# 3.
# ~ 10 이하	정상
# ~ 20 이하	과체중
# 20 ~ 초과	비만
bmi = int(input("bmi를 입력하세요:"))
if bmi <= 10:   # ~10
    print("정상")
elif bmi <= 20:  # 11 ~ 20
    print("과체중")
else:            # 21 ~
    print("비만")


# 4.
month = int(input("월을 입력하세요: "))

if month == 3 or month == 4 or month == 5:
    print("봄")
elif month == 6 or month == 7 or month == 8:
    print("여름")
elif month == 9 or month == 10 or month == 11:
    print("가을")
elif month == 12 or month == 1 or month == 2:
    print("겨울")
