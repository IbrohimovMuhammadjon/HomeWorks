_ = input()
nums = list(map(int, input().split()))
nums.sort()
ans = None
for i in range(len(nums) - 1, 1, -1):
    if nums[i] < nums[i - 1] + nums[i - 2]:
        ans = [nums[i - 2], nums[i - 1], nums[i]]
        break

if ans is not None:
    for num in ans:
        print(num, end=" ")
else:
    print(-1)


