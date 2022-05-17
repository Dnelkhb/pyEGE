s = []
for a1 in range(-100, 100):
    for a2 in range(-100, 100):
        fl = True
        for x in range(-100, 100):
            if not(((a1 <= x <= a2) <= ((x ** 2) <= 100)) and (((x ** 2) <= 64) <= (a1 <= x <= a2))):
                fl = False
                break
        if fl:
           s.append(a2 - a1)
print(min(s))