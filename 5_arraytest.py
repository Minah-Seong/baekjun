# 최소, 최대 (10818번)

length = int(input())
num = list(map(int, input().split()))
print(min(num), max(num))


# 최댓값 (2562번)

list1 = []

for i in range(9):
    new = int(input())
    list1.append(new)

print(max(list1))
print(list1.index(max(list1))+1)

# i 변수에 in 다음 리스트(문자열, 튜플)이 삽입되는 것임 i 위치는 변수다!


# 숫자의 개수 (2577번)

A = int(input())
B = int(input())
C = int(input())

num = list(str(A * B * C))
for i in range(0, 10):
    x = str(i)
    result = num.count(x)
    print(result)

# list 함수는 따로 split 하지 않아도 자동으로 문자열 분해해줌


# 나머지 (3052번)

# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다.
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

nums = []
for i in range(10):
    new_num = int(input())
    div_num = str(new_num % 42)
    if div_num not in nums:
        nums.append(div_num)

print(len(nums))







