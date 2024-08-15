hex_num = int(input())

num = int(f"0o{hex_num}", 8)

bin_num = bin(num)[2:]
print(bin_num)