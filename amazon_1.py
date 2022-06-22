def countFamilyLogins(logins):
    cnt = 0

    converted = []
    for login in logins:
        converted.append(convert(login))

    for i in range(len(logins)):
        for j in range(i + 1, len(logins)):
            if i == j:
                continue
            if is_adjacent(logins[i], logins[j]) and (convert(logins[i]) == convert(logins[j])):
                cnt += 1

    return cnt


def convert(login):
    ordered = [ord(l) for l in login]
    min_num = min(ordered)
    converted = [int(ordered[i]) - min_num for i, num in enumerate(ordered)]

    return converted


def is_adjacent(login1, login2):
    for i in range(len(login1)):
        l1, l2 = ord(min(login1[i], login2[i])), ord(max(login1[i], login2[i]))
        t1 = l1 + 1
        if t1 > 122:
            t1 -= 26
        t2 = l1 - 1
        if t2 < 97:
            t2 += 26
        if t1 != l2 and t2 != l2:
            return False

    return True


l0 = ["bag", "sfe", "cbh", "cbh", "red"]
l1 = ["corn", "horn", "dpso", "eqtp", "corn"]
l2 = ["cbu", "bat", "cbu"]
l3 = ["dba"]
l4 = ["dba", "dba", "dba", "dba", "dba"]
l5 = ["z", "a"]

print(countFamilyLogins(l0))
print(countFamilyLogins(l1))
print(countFamilyLogins(l2))
print(countFamilyLogins(l3))
print(countFamilyLogins(l4))
print(countFamilyLogins(l5))
