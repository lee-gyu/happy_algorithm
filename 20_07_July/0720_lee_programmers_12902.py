# 7월 20일

# 3 x n 타일링
# https://programmers.co.kr/learn/courses/30/lessons/12902
# 연습문제 - lv4
# DP 문제

# 이 문제는 함정이 있어보인다.
# n이 홀수가 되면 만들 수 있는 배열이 없다는 점이다.
# 에를 들어 타일의 크기가 3(3x1)이라면 이것은 2로 나누어 지지 않는다.
# 그리고 각 2마다 배치할 수 있는 기본 타일 종류가 3가지이다.
# 또한, 2가 늘어날 때마다 배치할 수 있는 고유 경우의 수가 2가지씩 늘어난다.
# 2가지씩 늘어나는 것에 대해서도 이전 경우의 수를 더해주어야 하는 것이 이전 2 x n 문제와의 차이이다.
# 짝수마다 고유의 경우를 2가지씩 만들고, 그 이전에 있던 경우의 수에서 또 새로운 경우의 만들어져
# 꽤나 연산이 많은 점화식이 성립된다.

# 규칙성 찾는 것에 연구를 많이 하자!
# DP는 역시 소스가 대부분 짧다.

# 점화식 d[n] = 2 + (d[n-2] * 3) + (d[n-4] * 2) + (d[n-6] * 2) ... 

# O(n^2)


def solution(n):
    if n % 2 != 0:
        return 0

    d = [0] * (n + 1)
    d[2] = 3

    
    for i in range(4, n + 1, 2):

        # 이전 결과에서 d[2]인 3가지 경우를 기본적으로 더 만들 수 있다.
        d[i] = (d[i - 2] * 3) % 1000000007
        
        # 기존의 d[2]에서 d[4]... d[n]까지 경우의 수를 또 만들어낼 수 있다.
        for j in range(i - 4, 0, -2):
            d[i] = (d[i] + (d[j] * 2) % 1000000007 ) % 1000000007

        # 현재 결과에서 추가로 만들 수 있는 2가지
        d[i] = (d[i] + 2) % 1000000007

    return d[n]

print(solution(4))
print(solution(6))
print(solution(8))
