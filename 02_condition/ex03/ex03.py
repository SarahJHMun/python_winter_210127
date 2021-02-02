weight = int(input("몸무게를 입력하세요:"))

# if - else문: if조건이 아닌 모든 경우
if weight <= 60:
    print("치킨")
else:
    print("샐러드")

# if - elif - else문
if weight <= 70:
    print("치킨")
elif weight <= 75:     # 71 ~ 75
    print("닭가슴살")
elif weight <= 80:    # 76 ~ 80
    print("샐러드")
else:  # 81 ~~
    print("굶자")

