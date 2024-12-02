MAX_WIDTH = 1000
MOD = 10007

width = int(input())

dp = [0] * MAX_WIDTH

# 점화식
# dp[i] = dp[i-2] + dp[i-1]
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, width+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[width] % MOD)


