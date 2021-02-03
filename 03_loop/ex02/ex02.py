# 0 ~ 4 : 5개
for i in range(5):     # range(0, 5)    range(0, 5, 1)
    print("신보람", i)

# 1 ~ 5: 5개
for i in range(1, 6):
    print("안녕", i)

# 5 ~ 1: 5개
for i in range(5, 0, -1):  # 5 4 3 2 1
    print("모니터", i)

# 1+2+3+4+5+6+7+8+9+10 합계
sum = 0
for i in range(1, 11):
    sum += i

print(sum)

for i in range(1, 6):
    print(i, end=" ")

print()
print("수행 끝")
