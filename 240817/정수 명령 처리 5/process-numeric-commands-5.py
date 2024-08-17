n = int(input())

def get_command_and_number(line) -> (str, int|None):
    words = line.split()
    if len(words) == 1:
        return words[0], None
    else:
        return words[0], int(words[1])

seq = []
for _ in range(n):
    line = input()
    command, num = get_command_and_number(line)
    if command == "push_back":
        seq.append(num)
    elif command == "pop_back":
        seq.pop()
    elif command == "size":
        print(len(seq))
    elif command == "get":
        print(seq[num-1])