num, formation = map(int, input().split())

if formation == 2:
    print(bin(num)[2:])
elif formation == 8:
    print(oct(num)[2:])
elif formation == 16:
    print(hex(num)[2:])
else:
    print('invalid formation')