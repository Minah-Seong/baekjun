# 최소, 최대 (10818)

length = int(input())
num = list(map(int, input().split()))
print(min(num), max(num))


# 최댓값 (2562)

list1 = []

for i in range(9):
    new = int(input())
    list1.append(new)

print(max(list1))
print(list1.index(max(list1))+1)

# i 변수에 in 다음 리스트(문자열, 튜플)이 삽입되는 것임 i 위치는 변수다!






