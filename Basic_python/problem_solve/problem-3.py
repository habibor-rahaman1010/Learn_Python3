def minimize_number(n, nums):
    count = 0
    while True:
        for i in range(n):
            if nums[i] % 2 == 0:
                nums[i] = nums[i] // 2
            else:
                return count
        count += 1

n = int(input())
nums = list(map(int, input().split()))
print(minimize_number(n, nums))
