# 안녕하세요 3번쓰기
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")

print("=" * 50)

# while 반복문으로 3번 반복하기
i = 0   # 카운팅 변수
while i < 3:  # 0 1 2   => 3
    print("안녕", i)
    i = i + 1

# 0 ~ 4 : 5번     0 1 2 3 4
i = 0
while i < 5:
    print("딸기", i)
    i += 1    #i = i + 1

# 1 ~ 5 : 5번    1 2 3 4 5
i = 1
while i <= 5:
    print("수박", i)
    i += 1

# 5 ~ 0: 6번
i = 5
while i >= 0:  # 5 4 3 2 1 0 => 6
    print("컴퓨터", i)
    i -= 1   # i = i - 1

# 합계 구하기
# 1 + 2 + 3+ 4 + 5 + 6... + 10
sum = 0
i = 1
while i <= 10:   # 1 2 3 4 5 6 7 8 9 10
    sum += i  #sum = sum + i
    i += 1

print(sum)
