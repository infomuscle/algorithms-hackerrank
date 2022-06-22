def countFamilyLogins(logins):
    cnt = 0
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
    converted = []
    for i, num in enumerate(ordered):
        converted.append(int(ordered[i]) - min_num)

    return converted


def is_adjacent(login1, login2):
    if ord(login1[0]) + 1 == ord(login2[0]) or ord(login2[0]) + 1 == ord(login1[0]):
        return True
    return False


l1 = ["corn", "horn", "dpso", "eqtp", "corn"]
l2 = ["cbu", "bat", "cbu"]

print(countFamilyLogins(l1))
print(countFamilyLogins(l2))
