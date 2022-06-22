def findMaximumSustainableClusterSize(processingPower, bootingPower, powerMax):
    n = len(processingPower)

    front = 0
    for i in range(len(processingPower)):
        if net_power_consumption(processingPower[:i + 1], bootingPower[:i + 1], i + 1) <= powerMax:
            front = i + 1
        else:
            break

    rear = 0
    for i in range(len(processingPower)):
        if net_power_consumption(processingPower[n - 1 - i:], bootingPower[n - 1 - i:], i + 1) <= powerMax:
            rear = i + 1
        else:
            break

    return front if front >= rear else rear


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
