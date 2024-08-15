# N번 주어진 두 단어들 중 한 단머만 선택해서 나오는 모든 경우의 수 중, 각 알파벳별로 최대 몇뻔식 나오는지 출력
n = int(input())

char_nums = {chr(97+i):0 for i in range(26)}

for _ in range(n):
    word1, word2 = input().split()
    for i in range(26):
        char = chr(97+i)
        max_count = max(word1.count(char), word2.count(char))
        char_nums[char] += max_count

for count in char_nums.values():
    print(count)