n = int(input())
zeros = 0
pos = 0
neg = 0
for i in range(n):
    num = int(input())
    if num == 0:
        zeros += 1
    elif num > 0:
        pos += 1
    else:
        neg += 1
print(zeros, pos, neg)