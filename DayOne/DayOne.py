# We'll do day 1 in 1 line (just for fun)
print sum([1 if c == '(' else -1 if c == ')' else 0 for c in (open("./input")).read()])
