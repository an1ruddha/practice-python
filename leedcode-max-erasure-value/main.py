from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        list_temp = [nums[0]]        
        temp_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if num in list_temp:
                index = list_temp.index(num)
                for _ in range(index+1):
                    temp_sum -= list_temp.pop(0)            
            list_temp.append(num)
            temp_sum += num
            if max_sum < temp_sum:
                max_sum = temp_sum
        return max_sum

def main():
    obj = Solution()
    list_nums = [[4,2,4,5,6],
                 [5,2,1,2,5,2,1,2,5],
                 [10000,1,10000,1,1,1,1,1,1],
                 [20,19,20,1,2,3,4,5]]
    
    for nums in list_nums:
        print(obj.maximumUniqueSubarray(nums), " = ", nums)
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
