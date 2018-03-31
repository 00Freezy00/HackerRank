def array_left_rotation(a, n, k):
    targetIndex = k - 1
    if targetIndex == n - 1:
        return a
    else:
        return a[targetIndex + 1:] + a[:targetIndex] + [a[targetIndex]]


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k)
print(*answer, sep=' ')