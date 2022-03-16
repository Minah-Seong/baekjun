# 개와 고양이

print('|\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\__|')

print("\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")


# 입출력을 이용한 사칙연산

A, B = input().split()
print(int(A)+int(B))
# 입력되는 문자를 input()함수로 받고 split()함수로 나누어 A,B변수에 저장

A, B = input().split()
print(int(A)-int(B))

A, B = input().split()
print(int(A)/int(B))

A, B = input().split()
print(int(A)+int(B))
print(int(A)-int(B))
print(int(A)*int(B))
print(int(A)//int(B))
print(int(A)%int(B))

A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)


# 곱셈식

A = int(input())
B = int(input())
fst = A * (B % 10)
aa = B // 100
trd = A * aa
snd = A * ((B - (aa * 100)) // 10)

print(fst)
print(snd)
print(trd)
print(fst + 10 * snd + 100 * trd)












