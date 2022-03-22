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

words = input().upper()
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])