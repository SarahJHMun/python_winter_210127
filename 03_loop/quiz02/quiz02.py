# 1. 35 36 37 38 39 40
for i in range(35, 41):
    print(i, end=" ")
print()

# 2. 5 4 3 2 1 0 -1 -2 -3 -4 -5
for i in range(5, -6, -1):
    print(i, end=" ")
print()

# 3. 3 6 9 12 15 18 21 24 27 30 33 36 39 42 45 48
# (1)
for i in range(1, 51):   # 1 ~ 50
    if i % 3 == 0:   # 3의 배수
        print(i, end=" ")
print()

# (2)
for i in range(3, 51, 3):    # 3 6 9 12 15 18....
    print(i, end=" ")
print()

# 4. 1 ~ 100 사이의 7의 배수 개수를 구하세요.
count = 0
for i in range(1, 101):
    if i % 7 == 0:
        count += 1
print("7의 배수의 개수는", count)

# 5. 수를 입력 받아서 해당하는 단수의 구구단을 출력 하세요.
num = int(input("단수를 입력하세요:"))
for i in range(1, 10):
    print("%d X %d = %d" % (num, i, num * i))

