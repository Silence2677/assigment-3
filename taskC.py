a = int(input())
b = int(input())

start = int(a**0.5)
if start * start < a:
    start += 1

res = []
i = start
while i * i <= b:
    res.append(i * i)
    i += 1

print(*res)