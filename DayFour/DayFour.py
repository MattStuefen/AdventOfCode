import hashlib


def find_hash_value(secret_key, starts_with="00000"):
    i = 1
    while not hashlib.md5(secret_key + str(i)).hexdigest().startswith(starts_with):
        i += 1
    return secret_key + str(i)


print "Example 1 test: " + str(find_hash_value("abcdef"))
print "Example 1 test: " + str(find_hash_value("pqrstuv"))
print "Final result: " + str(find_hash_value("iwrupvqb"))

print "Part 2 Final result: " + str(find_hash_value("iwrupvqb", "000000"))