k = int(input())
res = []

for i in range(1, k + 1):
    for j in range(i):
        if len(res) == k:
            break
        res.append(i)
    if len(res) == k:
        break

    print(*res)