# 구구단 출력
# 9 이하의 서로다른 정수 3개
# 가장 작은 수 부터 가장 큰 수까지 구구단 출력
# 중간값인 정수로 시작하는 구구단은 빼고 출력

nums = list(map(int, input().split()))

nums = sorted(nums)

for gu_num in range(nums[0], nums[-1] + 1):
    if gu_num == nums[1]:
        # 중간 숫자면 건너뜀
        continue
    for i in range(1, 10):
        print(f"{gu_num} * {i} = {gu_num * i}")