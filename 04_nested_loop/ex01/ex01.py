# 중첩 반복문:
#   - 밖에 있는 반복문: 천천히 돈다. ex) 세트   -- 행
#   - 안에 있는 반복문: 빨리 돈다. ex) 횟수    -- 열

# 벤치프레스 10회
for i in range(10):  # range(0, 10)
    print("벤치프레스 %d회" % (i + 1))

# 벤치프레스 3세트 10회씩
for i in range(1, 4):  # 1 2 3 세트
    for j in range(1, 11):  # 1 ~ 10회
        print("%d세트째 %d회" % (i, j))

# *****
# for i in range(5):
#     print("*", end="")

# *****
# *****
# *****
for i in range(3):   # 행   0 1 2
    for j in range(5):  # 열(별의 개수) 0 1 2 3 4
        print("*", end="")
    print()  # 줄바꿈
