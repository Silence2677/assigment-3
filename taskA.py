a = int(input())
b = int(input())

start = a + (a %2)

print(*(range(start, b + 1, 2 )))