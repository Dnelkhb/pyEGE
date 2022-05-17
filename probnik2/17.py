a = [int(x) for x in open('17(1).txt')]
s = []
m = 0
for i in range(len(a)-2):
    if (a[i] ** 2 + a[i+1] ** 2) == a[i+2] ** 2:
        s.append(a[i] + a[i+1] + a[i+2])
if len(s) == 0:
    m = 0
else:
    m = max(s)
print(len(s), m)
