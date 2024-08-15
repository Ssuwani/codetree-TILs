# 배열의 함을 구함
# N * N 크기의 숫자 배열이 주어짐,
# 각 행과 열 그리고 모든 요소의 합을 구하여 N * N 크기의 배열을 추가하여 n+1 * n+1 크기의 배열을 출력

num = int(input())

last_row_nums = [0] * num
for _ in range(num):
    row_nums = list(map(int, input().split()))
    for i in range(num):
        last_row_nums[i] += row_nums[i]
    for row in row_nums:
        print(row, end=" ")
    else:
        print(sum(row_nums))
else:
    for row in last_row_nums:
        print(row, end=" ")
    else:
        print(sum(last_row_nums))