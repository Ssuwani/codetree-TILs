n = int(input())

numbers = list(map(int, input().split()))

is_sorted = False
while is_sorted==False:
    is_sorted = True
    for i in range(n-1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            is_sorted = False
    

for num in numbers:
    print(num, end=" ")