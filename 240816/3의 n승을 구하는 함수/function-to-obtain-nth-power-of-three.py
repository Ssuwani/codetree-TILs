# 3의 n승을 구함
# 3**n을 구하는 프로그램을 재귀함수를 이용

n = int(input())
cnt = 0

def multiply(result):
    global cnt
    cnt += 1
    if cnt == n:
        print(result)
        return result
    else:
        result = multiply(result * 3)

multiply(3)