def goodSequence(n, numbers):
    if n == 1:
        return 1

    count = 0
    arra = []
    for i in range(1, n + 5):
        arra.append(0)

    for i in range(n):
        arra[numbers[i]] += 1

    for i in range(1, len(arra)):
        if arra[i] > 0:
            if i > arra[i]:
                count += arra[i]
            elif i < arra[i]:
                count += arra[i] - i

    return count


n = int(input())
numbers = list(map(int, input().split()))
print(goodSequence(n, numbers))