n = int(input())

numbers = list(map(int, input().split()))

for i in range(n):
    # n 번 반복
    # 가장 작은 값 찾기
    min_idx = i
    for j in range(i, n):
        if numbers[min_idx] > numbers[j]:
            min_idx = j
    
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

for num in numbers:
    print(num, end=" ")