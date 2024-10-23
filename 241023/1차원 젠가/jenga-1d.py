n = int(input())
genga = [int(input()) for _ in range(n)]

for _ in range(2):
    start, end = map(int, input().split())
    genga = genga[:start-1] + genga[end:]

print(len(genga))
for num in genga:
    print(num)