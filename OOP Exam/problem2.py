N, M = map(int, input().split())
A = list(map(int, input().split()))

frequencyArray = [0] * M

for num in A:
    frequencyArray[num - 1] += 1

for i in range(M):
    print(frequencyArray[i])
