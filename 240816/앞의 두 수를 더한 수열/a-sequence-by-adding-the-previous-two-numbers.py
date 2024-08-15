# 앞의 두 수를 더한 수열
# 첫번째 항이0, 두번째 항이 1인 수열
# 수열의 세번째 항 부터는 바로앞 두항의 합
# n이 주어졌을 때 n+1 번째 항을 구해라

# 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
n = int(input())
seq = [0, 1]
cnt = 0
while True:
    cnt += 1
    if cnt == n: break
    if n <= 1: break
    
    seq.append(seq[-1] + seq[-2])
    

print(seq[-1])