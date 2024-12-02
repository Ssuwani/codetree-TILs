# memoization으로 풀어보자

n = int(input())

# memo = [-1] * (n+1)

# def fibo(num):
#     if memo[num] != -1:
#         return memo[num]
#     if num == 1 or num == 2:
#         return 1
    
#     return fibo(num-1) + fibo(num-2)

# print(fibo(n))

dp = [0] * (n+1)

dp[1] = 1
dp[2] = 1

for i in range(3, n):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[-1])
