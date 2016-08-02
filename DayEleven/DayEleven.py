def find_next_password(password):
    password = increment_password(password)
    while not check_password(password):
        password = increment_password(password)
    return password


def increment_password(password):
    if len(password) == 0:
        return 'a'
    elif password[-1] == 'z':
        return increment_password(password[:-1]) + 'a'
    else:
        return password[:-1] + chr(ord(password[-1]) + 1)


def check_password(password):
    if ('i' in password) or ('o' in password) or ('l' in password): return False

    increasing_straight = False
    pair_sets = set()

    for i in range(len(password) - 1):
        increasing_straight |= (i != (len(password) - 2)) and\
                               (ord(password[i]) == (ord(password[i + 1]) - 1)) and\
                               (ord(password[i]) == (ord(password[i + 2]) - 2))
        if password[i] == password[i + 1]:
            pair_sets.add(password[i])

    return increasing_straight and (len(pair_sets) >= 2)


print "Example 1 test: " + increment_password('xx')
print "Example 2 test: " + increment_password('xy')
print "Example 3 test: " + increment_password('xz')
print "Example 4 test: " + increment_password('ya')

print "Example 5 test: " + 'hijklmmn - ' + str(check_password('hijklmmn'))
print "Example 6 test: " + 'abbceffg - ' + str(check_password('abbceffg'))
print "Example 7 test: " + 'abbcegjk - ' + str(check_password('abbcegjk'))

print "Example 8 test: " + find_next_password('abcdefgh')
print "Example 9 test: " + find_next_password('ghijklmn')

print "Final result: " + find_next_password('cqjxjnds')
print "Part 2 Final result: " + find_next_password('cqjxxyzz')