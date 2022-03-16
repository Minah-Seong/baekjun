# 구구단 (2739)
import sys

aa = int(input())
for i in range(1,10):
    print(aa, "*", i, "=", aa *  i)


# A+B-3 (10950)

i = int(input())
for i in range(i):
    A, B = map(int, input().split())
    print(A+B)


# 합 (8393)

i = 1
n = int(input())
aa = 0
for i in range(n + 1):
    aa = aa + i
    i = i + 1
print(aa)


# 1초 안에 실행 하는 빠른 A+B (15552)

import sys # sys 모듈 읽어들이기

n = int(sys.stdin.readline())
for i in range(n):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)


# N 찍기 (2741)

import sys

n = int(sys.stdin.readline())
i = 1
for i in range(1,n+1):
    print(i)
    i = i + 1


# 기찍 N (2742)

import sys

n = int(sys.stdin.readline())
i = n
for i in range(n,0,-1):
    print(i)
    i = i - 1


# A+B -7 (11021)

import sys

n = int(sys.stdin.readline())
for i in range(1, n + 1):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #", i, ": ", A + B, sep="")


# A+B -8 (11022)

import sys

n = int(sys.stdin.readline())
for i in range(1, n + 1):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #", i, ": ", A, " + ", B, " = ", A + B, sep="")


# 별 찍기 - 1 (2438)

import sys

n = int(sys.stdin.readline())
for i in range(1, n + 1):
    print('*' * i)


# 별 찍기 - 2 (2439)

import sys
a = int(sys.stdin.readline())

for i in range(1, a+1):
    print(" "*(a-i), "*"*i)

# 왼쪽 정렬 : ljust(전체 자리 수)
# 오른쪽 정렬 : rjust(전체 자리 수)


# X보다 작은 수 (10871)

aa, bb = map(int, input().split())
num = list(map(int, input().split()))

for i in range(aa):
    if num[i] < bb:
        print(num[i], end=" ")

