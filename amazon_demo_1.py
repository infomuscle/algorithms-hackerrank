def minimalHeaviestSetA(arr):
    arr.sort(reverse=True)

    sum_total = sum(arr)
    sum_a = 0
    list_a = []
    for element in arr:
        list_a.append(element)
        sum_a += element
        sum_total -= element
        if sum_a > sum_total:
            return sorted(list_a)


a1 = [3, 7, 5, 6, 2]
a2 = [5, 3, 2, 4, 1, 2]
a3 = [4, 2, 5, 1, 6]

print(minimalHeaviestSetA(a1))
print(minimalHeaviestSetA(a2))
print(minimalHeaviestSetA(a3))