class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        starters = [0,1]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] + nums[j] == target):
                    starters[0], starters[1] = i,j
                    break

        return starters