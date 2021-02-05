# 함수 사용하기
#   input이 무엇이고, output 무엇인지

# 1. 출력하기
print()   # 줄바꿈
print("안녕하세요")   # 전달 인자값, 인수(argument)

# 2. 길이 구하기
length = len("python")
print(length)

numbers = (1, 2, 3)
print(len(numbers))

# 3. 몫과 나머지 구하는 함수
q, r = divmod(20, 3)
print("몫:%d, 나머지:%d" % (q, r))
