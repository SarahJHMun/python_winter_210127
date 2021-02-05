
# 정수를 입력 받아서 2제곱의 결과를 돌려주는 함수를 만들고 호출한 값을 출력하세요.
# 5의 제곱은 25이다.
def squared(n):
    return n ** 2

number = int(input("수를 입력하세요"))
result = squared(number)
print("%d의 제곱은 %d이다." % (number, result))

# 2. 4개의 값을 받아서 평균을 돌려주는 함수를 만들고 호출한 값을 출력하세요.
def get_average(s1, s2, s3, s4):
    return (s1 + s2 + s3 + s4) / 4

def get_average_many(*scores):
    sum = 0
    for score in scores:
        sum += score
    return sum / len(scores)

s1, s2, s3, s4 = input("점수 4개를 입력하세요:").split()
s1 = int(s1)
s2 = int(s2)
s3 = int(s3)
s4 = int(s4)

average = get_average_many(s1, s2, s3, s4, 100, 95)
print("평균은 %g입니다." % average)

get_average_many(19,20, 59)

# 3. 두 수를 받아서 몫과 나머지를 출력하는 함수를 만드세요. (리턴값 없음)
def division(x, y):
    q = x // y
    r = x % y
    print("몫 : %d 나머지 : %d" % (q, r))

a, b = input("숫자와 나눌 수를 입력하세요:").split()
a = int(a)
b = int(b)
division(a, b)

# 4. 정수를 입력 받아서 '짝수'인지 '홀수'인지 돌려주는 함수를 만드세요.
def odd_even(n):
    if n % 2 == 0:
        return "짝수"
    return "홀수"

number = int(input("수를 입력하세요:"))
print(odd_even(number))



