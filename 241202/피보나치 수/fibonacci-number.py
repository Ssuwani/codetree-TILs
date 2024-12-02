# memoization으로 풀어보자

n = int(input())

memo = [-1] * (n+1)

def fibo(num):
    if memo[num] != -1:
        return memo[num]
    if num == 1 or num == 2:
        return 1
    
    return fibo(num-1) + fibo(num-2)

print(fibo(n))