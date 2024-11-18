"""

DFS 그래프 상에서 정의됨
그래프랑 정점과 간선으로 이루어져 있는 자료구조

array = [
    [0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    ...
]
N개의 정점
M개의 간선
양방향 그래프가 주어짐

1번에서 시작해서 간선을 따라 이동했을 때 도달할 수 있는 정점의 수를 구해
(자기 자신은 제외)

"""

n, m = map(int, input().split())

# 인접 리스트
ll = [[] for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int, input().split())
    ll[n1].append(n2)
    ll[n2].append(n1)
visited = [False] * (n+1)
answer = 0
def dfs(curr):
    global answer
    
    for n in ll[curr]:
        if visited[n]:
            continue
        answer += 1
        visited[n] = True 
        dfs(n)
visited[1] = True
dfs(1)
print(answer)