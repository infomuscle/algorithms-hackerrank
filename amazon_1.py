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
    return ord(login1[0]) + 1 == ord(login2[0]) or ord(login2[0]) + 1 == ord(login1[0])


l0 = ["bag", "sfe", "cbh", "cbh", "red"]
l1 = ["corn", "horn", "dpso", "eqtp", "corn"]
l2 = ["cbu", "bat", "cbu"]
l3 = ["dba"]

print(countFamilyLogins(l0))
print(countFamilyLogins(l1))
print(countFamilyLogins(l2))
print(countFamilyLogins(l3))
