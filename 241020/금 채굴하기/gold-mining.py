n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
] # 금 있는 게 1 없는 게 0

# 금 한개의 가격이 M

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def get_gold_count(x, y, K) -> int:
    gold_cnt = 0

    def _get_gold(x, y) -> bool:
        return in_range(x, y) and grid[x][y]

    for dx in range(K+1):
        for dy in range(K-dx+1):

            if _get_gold(x + dx, y + dy):
                gold_cnt += 1
            
            if dx and _get_gold(x - dx, y + dy):
                gold_cnt += 1

            if dy and _get_gold(x + dx, y - dy):
                gold_cnt += 1

            if dx and dy and _get_gold(x - dx, y - dy):
                gold_cnt += 1
    return gold_cnt

max_gold = 0
for i in range(n):
    for j in range(n):
        for K in range(0, n+1):
            price = K * K + (K + 1) * (K + 1)
            gold_cnt = get_gold_count(i, j, K)
            profit = m * gold_cnt

            if profit >= price:
                max_gold = max(max_gold, gold_cnt)
print(max_gold)