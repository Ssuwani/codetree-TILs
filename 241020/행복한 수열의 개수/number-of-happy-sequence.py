n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
if m == 1:
    print(2*n)
else:
    grid_T = list(map(list, zip(*grid)))

    happy = 0
    for line in grid:
        for i in range(n - m + 1):
            if len(set(line[i: i+m])) == 1:
                happy += 1

    for line in grid_T:
        for i in range(n - m + 1):
            if len(set(line[i: i+m])) == 1:
                happy += 1
                break

    print(happy)