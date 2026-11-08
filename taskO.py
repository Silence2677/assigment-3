n = int(input())
has_zero = false
for i in range(n):
    if int(input()) == 0:
        has_zero = True

if has_zero:
    print("yes")
else:
    print("no")