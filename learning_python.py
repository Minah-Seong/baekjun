# A+B - 2 (2558번)

a = int(input())
b = int(input())
print(a+b)


# R2 (3046번)

a, b = map(int, input().split())
print(2 * b - a)


# 초콜릿 자르기 (2163번)

# 정화는 N×M 크기의 초콜릿을 하나 가지고 있다. 초콜릿은 금이 가 있는 모양을 하고 있으며,
# 그 금에 의해 N×M개의 조각으로 나눠질 수 있다.
# 초콜릿의 크기가 너무 크다고 생각한 그녀는 초콜릿을 친구들과 나눠 먹기로 했다.
# 이를 위해서 정화는 초콜릿을 계속 쪼개서 총 N×M개의 조각으로 쪼개려고 한다.
# 초콜릿을 쪼갤 때에는 초콜릿 조각을 하나 들고, 적당한 위치에서 초콜릿을 쪼갠다.
# 초콜릿을 쪼갤 때에는 금이 가 있는 위치에서만 쪼갤 수 있다.
# 이와 같이 초콜릿을 쪼개면 초콜릿은 두 개의 조각으로 나눠지게 된다.
# 이제 다시 이 중에서 초콜릿 조각을 하나 들고, 쪼개는 과정을 반복하면 된다.
# 초콜릿을 쪼개다보면 초콜릿이 녹을 수 있기 때문에, 정화는 가급적이면 초콜릿을 쪼개는 횟수를 최소로 하려 한다.
# 초콜릿의 크기가 주어졌을 때, 이를 1×1 크기의 초콜릿으로 쪼개기 위한 최소 쪼개기 횟수를 구하는 프로그램을 작성하시오.

a, b = map(int, input().split())
print(a*b-1)


# 오늘 날짜 (10699번)

from datetime import datetime

today = str(datetime.now())[:10]
print(today)


# 등록 (7287번)

print(57)
print('sma0608')


# 인공지능 시계 (2530번)

# KOI 전자에서는 건강에 좋고 맛있는 훈제오리구이 요리를 간편하게 만드는 인공지능 오븐을 개발하려고 한다.
# 인공지능 오븐을 사용하는 방법은 적당한 양의 오리 훈제 재료를 인공지능 오븐에 넣으면 된다. 그러면 인공지능 오븐은 오븐구이가 끝나는 시간을 초 단위로 자동적으로 계산한다.
# 또한, KOI 전자의 인공지능 오븐 앞면에는 사용자에게 훈제오리구이 요리가 끝나는 시각을 알려 주는 디지털 시계가 있다.
# 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 초 단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.

a, b, c = map(int, input().split())
sec = int(input())

c_sec = c + sec

if c_sec >= 60:
    b += c_sec // 60
    c = c_sec % 60
    if b >= 60:
        a += b // 60
        b = b % 60
        if a >= 24:
            a = a % 24
else:
    c = c_sec

print(a, b, c)


# 저작권 (2914번)

a, b = map(int, input().split())
print(a*(b-1)+1)


# 화성 수학 (5355번)

n = int(input())
for _ in range(n):
    count = list(map(str, input().split()))
    result = 0
    for i in range(len(count)):
        if i == 0:
            result += float(count[i])
        else:
            if count[i] == '@':
                result *= 3
            elif count[i] == '#':
                result -= 7
            elif count[i] == '%':
                result += 5
    print("%0.2f" % result)




