def solution(nums):
    answer = 0
    size = len(nums)//2
    nums=list(set(nums))
    if len(nums) > size:
        return size
    else:
        return len(nums)

nums = [3,1,2,3]
print(solution(nums))