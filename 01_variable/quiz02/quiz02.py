# 1. 아래 정수와 실수를 곱해서 출력하세요
number1 = 33
number2 = 35.325
result = number1 * number2
print("두 수의 곱은 %f 입니다." % result)

# 2. 943 시간은 몇일 몇시간 인지 구하여 출력하세요.
# 943시간은 39일 7시간 입니다.
hour = 943
d = hour // 24
h = hour % 24
print("%d시간은 %d일 %d시간 입니다." % (hour, hour // 24, hour % 24))

# 3. 도형 넓이 구하기
# 가로 길이 8 세로 길이 9인 사각형과 삼각형의 넓이
width = 8
height = 9
rectangle_area = width * height
triangle_area = width * height / 2
# 사각형의 넓이 : 72
# 삼각형의 넓이 : 36
print("사각형의 넓이 :", rectangle_area)
print("삼각형의 넓이 :", triangle_area)


