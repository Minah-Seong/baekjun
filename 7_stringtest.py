# 아스키 코드 (11654번)

str1 = input()
print(ord(str1))

# 숫자 -> 문자 변환 함수 : chr()


# 숫자의 합 (11720번)

n = int(input())
numbers = int(input())
a = 0
for i in str(numbers):
    a += int(i)
print(a)


# 알파벳 찾기 (10809번)

from string import ascii_lowercase

alpha_list = list(ascii_lowercase)
word = input()
word_list = list(word)
for i in alpha_list:
    if i in word_list:
        print(word_list.index(i), end=' ')
    else:
        print(-1, end=' ')


# 문자열 반복 (2675번)

n = int(input())
for _ in range(n):
    ex = input().split()
    num = int(ex[0])
    word = list(ex[1])
    for i in word:
        print(i*num, end='')
    print()


# 단어 공부 (1157번)




