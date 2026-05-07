class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        foundDuplicate = False
        d = {}

        for i in range(len(nums)):
            if nums[i] in d:
                foundDuplicate = True
                break

            d[nums[i]] = i

        return foundDuplicate