# 1. 두 점수를 입력 받고, 평균이 70점 이상이면 합격 그렇지 않으면 불합격을 출력하세요.
# score1, score2 = input("두 점수를 입력하세요:").split()
# score1 = int(score1)
# score2 = int(score2)
# average = (score1 + score2) / 2
# if average >= 70:
#     print("합격")
# else:
#     print("불합격")

# 2. 세 개의 정수를 입력 받아서 가장 큰 값을 출력하세요.
# a, b, c = input("세 개의 정수를 입력하세요:").split()
# a = int(a)   # 1
# b = int(b)   # 3
# c = int(c)   # 5
#
# max = a
# if max < b:
#     max = b
# if max < c:
#     max = c
# print(max)

# 3.
# 평균이 60점 이상이면 합격
#   한과목이라도 50점 이하면 무조건 과락
# 평균 60점 미만이면 불합격
# score1 = int(input("점수1:"))
# score2 = int(input("점수2:"))
# average = (score1 + score2) / 2
# if average < 60:
#     print("불합격")
# else:  # 평균 60점 이상
#     if score1 <= 50 or score2 <= 50:
#         print("과락")
#     else:
#         print("합격")

# 4로 나누어 떨어지는 연도는 윤년이다.
# 100으로 나누어 떨어지는 연도는 윤년이 아니다.
# 400으로 나누어 떨어지는 연도는 무조건 윤년이다.
year = int(input("연도:"))
# (1)
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("윤년")
        else:
            print("평년")
    else:
        print("윤년")
else:
    print("평년")

# 4로 나누어 떨어지는 연도는 윤년이다.-
#  100으로 나누어 떨어지는 연도는 윤년이 아니다.-
# 400으로 나누어 떨어지는 연도는 무조건 윤년이다.-
# (2)
if year % 400 == 0:
    print("윤년")
elif year % 100 == 0:
    print("평년")
elif year % 4 == 0:
    print("윤년")
else:
    print("평년")

# 4로 나누어 떨어지고 그리고 100으로 나누어 떨어지지 않는 연도는 윤년
# 또는
# 400으로 나누어 떨어지는 연도는 무조건 윤년이다.
# (3)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("윤년")
else:
    print("평년")
    
# 5
stick1, stick2, stick3, stick4 = input("윷 상태를 입력하세요: ").split()
stick1 = int(stick1)
stick2 = int(stick2)
stick3 = int(stick3)
stick4 = int(stick4)

cnt = stick1 + stick2 + stick3 + stick4

if cnt == 1:
    print("도")
elif cnt == 2:
    print("개")
elif cnt == 3:
    print("걸")
elif cnt == 4:
    print("윷")
else:
    print("모")
