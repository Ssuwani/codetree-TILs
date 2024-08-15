# 1까지 나누는 재귀함수
# 정수 n
# 짝수면 2, 홀수면 3으로 나눠 목을 취함
# n이 1이 될 때까지 반복
# 나오는 결과를 출력

n = int(input())
print(n, end=" ")
def transform(num):
    if num % 2 ==0:
        # 짝수면
        return num // 2
    else:
        # 홀수면
        return num // 3

while True:
    n = transform(n)    
    print(n, end=" ")
    if n == 1:
        break