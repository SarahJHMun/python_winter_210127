# 함수 만들기
# input -> 구현 -> output
# 1. 무슨 함수를 만들지 => 함수명을 짓는다  (함수명 규칙: snake case)
# 2. input을 무엇으로 받을지
# 3. output을 무엇으로 돌려줄건지
# 4. 구현하기

# 함수 구현
def sum(x, y):   # 매개변수 (parameter)
    return x + y

# 몇 개의 정수를 더할지 모른다면
def add_many(*values):
    sum = 0
    for i in values:    # 2 5 6
        sum += i
    return sum

# 리턴값이 없는 함수
def minus(x, y):
    print("%d에서 %d를 뺀 값은 %d입니다." % (x, y, x - y))

# 사용하는 곳
a, b = input("더할 수 두개를 입력하세요:").split()
a = int(a)
b = int(b)
result = sum(a, b)
print("합계:", result)

print(add_many(a, b, 10, 90, 45, 10))

minus(100, 60)
