# 두 수 비교하기

A, B = map(int, input().split())
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")


# 시험 성적

score = int(input())
if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score < 90:
    print("B")
elif score >= 70 and score < 80:
    print("C")
elif score >= 60 and score < 70:
    print("D")
else:
    print("F")


# 윤년

year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(1)
else:
    print(0)


# 사분면 고르기

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)


# 알람 시계

H, M = map(int, input().split())

M = M - 45
if M < 0:
    H = H - 1
    M = 60 - ((-1) * M)
    if H < 0:
        H = 24 - H * (-1)

print(H, M)


# 오븐 시계 (2525)

A, B = map(int, input().split())
C = int(input())

A += C // 60
B += C % 60

if B >= 60:
    A += 1
    B -= 60
if A >= 24:
    A -= 24

print(A, B)


# 주사위 세개 (2480)


A, B, C = map(int, input().split())

if A == B and B == C and C == A:
    price = 10000 + (A * 1000)
elif A == B:
    price = 1000 + (A * 100)
elif B == C:
    price = 1000 + (B * 100)
elif C == A:
    price = 1000 + (C * 100)
else:
    price = max(A, B, C) * 100

print(price)

