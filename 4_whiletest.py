# A + B - 5 (10952)

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a + b)


# A + B - 4 (10951)

import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except:
        break

# 파이썬 예외 처리 구문 try, except 상황








# 더하기 사이클 (1110)

import sys

n = int(sys.stdin.readline())
origin = n
i = 0

while True:
    fst = n % 10
    snd = n // 10
    aa = snd + fst
    bb = (fst * 10) + (aa % 10)
    i = i + 1
    n = bb
    if bb == origin:
        break
print(i)


