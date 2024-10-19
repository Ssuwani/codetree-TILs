n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def get_coin_count(x, y) -> int:
    coin_count = 0
    for line in grid[x: x+3]:
        coin_count += sum(line[y:y+3])
    return coin_count

def in_range(x, y):
    return 0 <= x < n-2 and 0 <= y < n-2

max_coin = 0
for i in range(n):
    for j in range(n):
        if in_range(i, j):
            max_coin = max(max_coin, get_coin_count(i, j))
print(max_coin)