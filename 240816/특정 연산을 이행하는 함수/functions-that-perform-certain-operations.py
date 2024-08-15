# 3개의 정수가 주어짐
# 짝수인 경우 2로 나눠서 출력, 
# 홀수인 경우 3을 곱한 뒤 -20 하여 출력

num1, num2, num3 = map(int, input().split())

def transform(num):
    if num % 2 == 0:
        # 짝수
        return num // 2
    else:
        # 홀수
        return num * 3 - 20

print(transform(num1), transform(num2), transform(num3))