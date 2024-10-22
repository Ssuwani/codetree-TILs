n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
b = list(map(int, input().split()))

for _ in range(t):
    l, r, b = [b[-1]] + l[:-1], [l[-1]] + r[:-1], [r[-1]] + b[:-1]

for n in l:
    print(n, end=" ")
print()

for n in r:
    print(n, end=" ")
print()

for n in b:
    print(n, end=" ")