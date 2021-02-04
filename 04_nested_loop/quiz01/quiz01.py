# 1. 두 개의 주사위를 굴렸을 때, 나올 수 있는 모든 경우의 수를 출력하세요.
for i in range(1, 7):  # 1 ~ 6
    for j in range(1, 7):  # 1 ~ 6
        print("(%d, %d)" % (i, j), end=" ")
    print()

# 2. 2~9 구구단
# 바깥 반복문: 단수
# 안쪽 반복문: 1~9 곱해지는 수
for i in range(2, 10):  # 단수
    for j in range(1, 10): # 곱해지는 수
        print("%d X %d = %d" % (i, j, i * j))

# 3.
# *        행:1     별:1개
# **       행:2     별:2개
# ***
# ****
# *****    행:5     별:5개
for i in range(1, 6):  # 행
    for j in range(i):  # 별의 개수, 열
        print("*", end="")
    print()

print("=" * 50)

for i in range(1, 6):
    print("*" * i)
