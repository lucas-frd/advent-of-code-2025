ranges = input().split(",")
invalid_ids = set()
for r in ranges:
    first_id, last_id = r.split("-")
    for id in range(int(first_id), int(last_id)+1):
        wasAdded = False
        for j in range(1, len(str(id)) // 2 + 1):
            if wasAdded:
                break
            if len(str(id)) % j != 0:
                continue
            else:
                wasAdded = True
                prev_value = str(id)[:j]
                for k in range(j, len(str(id)), j):
                    curr = str(id)[k:k+j]
                    if curr != prev_value:
                        wasAdded=False
                        break
                if wasAdded:
                    invalid_ids.add(id)
print(sum(invalid_ids))