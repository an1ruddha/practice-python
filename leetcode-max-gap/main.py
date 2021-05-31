from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        elif len(nums) == 2:
            return abs(nums[0] - nums[1])
        else:
            nums.sort()
            list_gap = set()
            for i in range(len(nums)-1):
                list_gap.add(nums[i+1] - nums[i])
            return max(list_gap)

def main():
    obj = Solution()
    list_nums = [[3,6,9,1],
                 [10]]
    
    for nums in list_nums:
        print(obj.maximumGap(nums), " = ", nums)
if __name__ == "__main__":
    main()

# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

# Return the maximum score you can get by erasing exactly one subarray.

# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

# Example 1:

# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].
# Example 2:

# Input: nums = [5,2,1,2,5,2,1,2,5]
# Output: 8
# Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104

