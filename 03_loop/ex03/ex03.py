# break문: break가 써진 가장 가까운 반복문에서 빠져나온다.
i = 0
while True:   # 0 1 2 3 4   => 5번
    if i == 5:
        break
    print("파이썬", i)
    i += 1

# continue문 : skip하는 조건. 아래의 코드는 실행하지 않음
# 1 ~ 10:  1 2 3 5 6 7 9 10
for i in range(1, 11):
    if i % 4 == 0:   # 4의 배수
        continue

    # 4의 배수가 아닌 숫자가 여기 도달한다.
    print(i, end=" ")
