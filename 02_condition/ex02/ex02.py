num = int(input("숫자를 입력하세요:"))

# 10 <= num <= 40 : num은 10 이상이고 40 이하이다
if 10 <= num <= 40:
    print("%d은 10 이상이고 40 이하이다" % num)

if num >= 10 and num <= 40:
    print("%d은 10 이상이고 40 이하이다" % num)

# num < 10 또는 num > 40 : num이 10보다 작거나 또는 num이 40보다 크다
if num < 10 or num > 40:
    print("%d이 10보다 작거나 또는 %d이 40보다 크다" % (num, num))




weight, walk = input("몸무게와 걸음수를 입력하세요:").split()
weight = int(weight)
walk = int(walk)

# 만약에 몸무게가 60키로 이하이고 걸은수가 10000보를 초과하면 "치킨"
if weight <= 60 and walk > 10000:
    print("둘 다 만족하니 치킨 먹자!")

# 만약에 몸무게가 60키로 이하이거나 걸은수가 10000보를 초과하면 "치킨"
if weight <= 60 or walk > 10000:
    print("하나라도 만족하니 치킨 먹자!")
