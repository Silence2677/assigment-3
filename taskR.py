a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

count = 0
for i in range(1001):
    if i != e and (a * i**3 + b * i**2 + c * i + d) == 0:
        count += 1

print(count)
