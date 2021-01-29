noodle_cup = 850
print("육개장 가격은", noodle_cup, "원 입니다.")

# format : 문자열 속에 다른 타입의 변수값을 넣을 때 사용
print("육개장 가격은 %d원 입니다." % noodle_cup)
# 육개장 하나의 가격은 O원이고 3개의 가격은 0원 입니다.
print("육개장 하나의 가격은 %d원이고 3개의 가격은 %d원 입니다." % (noodle_cup, noodle_cup * 3))

# 소수 (float)
pi = 3.14
print("원주율 pi는 %f입니다." % pi)

# 문자(Character) : 문자 한개를 의미
grade = "A"
print("등급은 %c 입니다." % grade)

# 문자열(String) : 문장
name = "신보람"
print("이름은 %s입니다." % name)

real_pi = 3.1415926535897
# 소수점 표시
print("원주율: %f" % real_pi)  # 소수점 아래 6자리까지 표시
print("소수점 둘째자리 원주율: %.2f" % real_pi) # 소수점 둘째자리 반올림
print("소수점 여덟째자리 원주율: %.8f" % real_pi) # 소수점 여덟째자리 반올림
print("원주율 pi는 %g 입니다." % real_pi)
print("%g" % 35.0)

# 100%
print("%d%%" % 100)
