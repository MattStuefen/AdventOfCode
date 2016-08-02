# We'll do day 1 (part 1) in 1 line (just for fun)
print sum([1 if c == '(' else -1 if c == ')' else 0 for c in (open("./input")).read()])

# Part 2
floor = 1
count = 0
for c in (open("./input")).read():
    floor += 1 if c == '(' else -1 if c == ')' else 0
    count += 1

    if floor == 0:
        break

print count
