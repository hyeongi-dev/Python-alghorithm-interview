#561 배열 파티션 1, 파이썬 알고리즘 인터뷰 10번
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0

        for idx in range(0,len(nums),2):
            sum += nums[idx]
            
        return sum
            