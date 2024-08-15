# 앞의 두 수를 더한 수열 2

# 첫번째 항1, 두번째항 1

seq = [1,1]


[seq.append(seq[-1] + seq[-2]) for i in range((int(input()))-2)]

print(seq[-1])