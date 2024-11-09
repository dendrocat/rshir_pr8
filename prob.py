def format(s):
    for i in range(len(s), -1, -3):
        print(s[max(i - 3, 0):i], i-3, i)


    return " ".join([s[max(i-3, 0):i] for i in range(len(s), 0,-3)][::-1])

print(format("100000"))