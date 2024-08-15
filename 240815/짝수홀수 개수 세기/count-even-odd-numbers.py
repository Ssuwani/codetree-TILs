n = int(input())
odd_cnt = 0
even_cnt = 0
for _ in range(n):
    num = int(input())
    if num == 0: break

    if num % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1
print(even_cnt)
print(odd_cnt)