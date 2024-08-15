numbers = map(float, input().split())
int_nums = [round(num) for num in numbers]

print(sum(int_nums))
print(round(sum(int_nums) / len(int_nums)))