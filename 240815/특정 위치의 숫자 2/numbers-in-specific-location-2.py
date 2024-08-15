n = int(input())

nums = list(map(int, input().split()))
nums = nums[1::2]

nums_sum = sum(nums)

print(nums_sum, round(nums_sum / len(nums), 1))