# n개의 정수가 주어지면 내림차순 정렬

_ = input()
nums = map(int, input().split())
for num in sorted(nums, reverse=True):
    print(num, end=" ")