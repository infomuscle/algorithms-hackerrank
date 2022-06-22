def findMaximumSustainableClusterSize(processingPower, bootingPower, powerMax):
    n = len(processingPower)

    front, rear = 0, 0

    max_k = 0
    while rear < n:
        k = rear - front + 1
        if net_power_consumption(processingPower[front:rear + 1], bootingPower[front: rear + 1], k) <= powerMax:
            max_k = max(k, max_k)
            rear += 1
        else:
            if rear > front:
                front += 1
            else:
                rear += 1
    return max_k


def net_power_consumption(processingPower, bootingPower, k):
    return max(bootingPower) + sum(processingPower) * k


p0 = [2, 1, 3, 4, 5]
b0 = [3, 6, 1, 3, 4]
m0 = 25

p1 = [4, 1, 4, 5, 3]
b1 = [8, 8, 10, 9, 12]
m1 = 33

print(findMaximumSustainableClusterSize(p0, b0, m0))
print(findMaximumSustainableClusterSize(p1, b1, m1))
