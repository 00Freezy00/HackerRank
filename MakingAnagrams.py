def number_needed(a, b):
    need2Del = 0
    a2z = dict.fromkeys('abcdefghijklmnopqrstuvwxyz', 0)
    for i in range(len(a)):
        a2z[a[i]] += 1
    for i in range(len(b)):
        a2z[b[i]] += 1
    for i in a2z:
        if a2z[i] != 2 and a2z[i] != 0:
            need2Del += 1
    return need2Del


a = input().strip()
b = input().strip()

print(number_needed(a, b))
