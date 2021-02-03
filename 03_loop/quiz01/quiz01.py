# 1. 수를 입력 받아서 그 수만큼 "화이팅!!!" 를 출력하세요
count = int(input("수를 입력하세요:"))   # 3
i = 0
while i < count:   # 0 1 2 => 3
    print("화이팅!!!")
    i += 1

# 2. 수를 입력 받고 그 수에서 부터 0까지 한 줄씩 카운트 다운을 출력 하고 마지막에 "발사"를 출력하세요.
count_down = int(input("카운트 다운을 입력하세요:"))  # 5
while count_down >= 0:
    print(count_down)
    count_down -= 1

print("발사")

# 3. while을 이용하여 5번 동안 수를 입력 받고 출력하세요.
i = 0
while i < 5:
    number = int(input("수를 입력하세요:"))
    print(number)
    i += 1

# 4.
# 3 X 1 = 3
# 3 X 2 = 6
# 3 X 3 = 9
num = 3
i = 1
while i <= 9:
    print("%d X %d = %d" % (num, i, num * i))
    i += 1
