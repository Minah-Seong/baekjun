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


# 단어의 개수 (1152번)

sen = input()
my_list = sen.split()
print(len(my_list))


# 상수 (2908번)

nums = map(int, input().split())
new_nums = []
for n in nums:
    a = str(n)
    b = list(a)
    c = list(map(int, b))
    new_n = c[0] + (10 * c[1]) + (100 * c[2])
    new_nums.append(new_n)
print(max(new_nums))


# 다이얼 (5622번)

# 전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
# 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
# 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

from string import ascii_uppercase

upper = list(ascii_uppercase)
abc = upper[0:3]
def_ = upper[3:6]
ghi = upper[6:9]
jkl = upper[9:12]
mno = upper[12:15]
pqrs = upper[15:19]
tuv = upper[19:22]
wxyz = upper[22:26]

word = input()
word_list = list(word)

result = []
for i in word_list:
    if i in abc:
        i = 3
        result.append(i)
    elif i in def_:
        i = 4
        result.append(i)
    elif i in ghi:
        i = 5
        result.append(i)
    elif i in jkl:
        i = 6
        result.append(i)
    elif i in mno:
        i = 7
        result.append(i)
    elif i in pqrs:
        i = 8
        result.append(i)
    elif i in tuv:
        i = 9
        result.append(i)
    else:
        i = 10
        result.append(i)
print(sum(result))

# 해답

dial_text = ['1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
gm = input()
t = 0

for i in gm:
    for j in dial_text:
        for k in j:
            if k == i:
                t = t + 2 + dial_text.index(j)
print(t)


# 크로아티아 알파벳 (2941번)

c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

search = input()
for i in c_alpha:
    search = search.replace(i, '*')

print(len(search))


# 그룹 단어 체커 (1316번)

# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

n = int(input())
group_word = []
for _ in range(n):
    word = input()
    word_list = list(word)
    count = 0
    for i in range(len(word_list) - 1):
        if word_list[i] != word_list[i + 1]:
            new_word = word_list[i + 1:]
            if word_list[i] in new_word:
                count += 1
    if count == 0:
        group_word.append(word)

print(len(group_word))





