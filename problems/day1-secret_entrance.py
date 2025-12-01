rotations = []
while True:
    cur = input()
    if cur == "break":
        break
    else:
        rotations.append(cur)

dial = 50
res = 0
for rot in rotations:
    direction, offset = rot[0], int(rot[1:])
    if direction == "L":
        dial -= offset
    else:
        dial += offset
    print(dial, dial // 100)
    res += abs(dial // 100)
    dial %= 100
print(res)

