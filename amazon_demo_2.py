from collections import deque


def countGroups(related):
    relation = []
    for row in related:
        relation.append([int(r) for r in row])

    cnt = 0

    ways = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    queue = deque()
    for i in range(len(relation)):
        for j in range(len(relation[i])):
            if relation[i][j] != 1:
                continue

            queue.append((i, j))
            while queue:
                current = queue.popleft()
                if current in visited:
                    continue
                relation[current[0]][current[1]] += 1
                relation[current[1]][current[0]] += 1
                visited.add(current)
                visited.add((current[1], current[0]))
                for way in ways:
                    reachable_pos = (current[0] + way[0], current[1] + way[1])
                    if (0 <= reachable_pos[0] < len(relation)) and (0 <= reachable_pos[1] < len(relation[i])) and (reachable_pos not in visited) and relation[reachable_pos[0]][reachable_pos[1]] == 1:
                        queue.append(reachable_pos)
            cnt += 1

    return cnt


r1 = ['1100', '1110', '0110', '0001']
r2 = ['10000', '01000', '00100', '00010', '00001']
r3 = ['1']

print(countGroups(r1))
print(countGroups(r2))
print(countGroups(r3))
