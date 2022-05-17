x = 125 + 25 ** 3 + 5 ** 9
k = 0
while x > 0:
    if x % 5 == 0:
        k += 1
    x //=5
print(k)