# 1. 1부터 n까지의 합
n = int(input("수를 입력하세요: "))

# (1) while
i = 0
sum = 0
while i <= n:
    sum += i
    i += 1
    

print("합은 %d입니다." % sum)

print("=" * 50)

# (2) for
sum = 0
for i in range(1, n + 1):
    sum += i

print("합은 %d입니다." % sum)


# 2. 팩토리얼
n = int(input("수를 입력하세요: "))

# (1) while
i = 2
fact = 1
while i <= n:
    fact *= i
    i += 1

print("%d!는 %d입니다." % (n, fact))

print("=" * 50)

# (2) for
fact = 1
for i in range(2, n + 1):
    fact *= i

print("%d!는 %d입니다." % (n, fact))

#3. 약수
n = int(input("수를 입력하세요: "))

# (1) while
i = 1
while i <= n:
    if n % i == 0:
        print(i, end = " ")

    i += 1

print()
print("=" * 50)

# (2) for
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end = " ")
