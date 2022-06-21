def countGroups(related):
    relation = []
    for row in related:
        relation.append([int(r) for r in row])

    groups = []
    for i in range(len(relation)):
        for j in range(len(relation)):
            if relation[i][j] >= 1:
                added = False
                for group in groups:
                    if (i in group or j in group) and not added:
                        group.add(i)
                        group.add(j)
                        added = True
                if not added:
                    groups.append({i, j})

    return len(groups)


r1 = ['1100', '1110', '0110', '0001']
r2 = ['10000', '01000', '00100', '00010', '00001']
r3 = ['1']

print(countGroups(r1))
print(countGroups(r2))
print(countGroups(r3))
