from typing import List

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dict_map = {}
        def check(s1, s2, s3, len_s1, len_s2, len_s3, p1, p2, p3):
            if p3 == len_s3:
                if p1 == len_s1 and p2 == len_s2:
                    return True
                else:
                    return False
            
            key = f"{p1}*{p2}*{p3}"

            if key in dict_map:
                return dict_map[key]
            
            if p1 == len_s1:
                if s2[p2] == s3[p3]:
                    dict_map[key] = check(s1, s2, s3, len_s1, len_s2, len_s3, p1, p2+1, p3+1)
                else:
                    dict_map[key] = False
                return dict_map[key]
            if p2 == len_s2:
                if s1[p1] == s3[p3]:
                    dict_map[key] = check(s1, s2, s3, len_s1, len_s2, len_s3, p1+1, p2, p3+1)
                else:
                    dict_map[key] = False
                return dict_map[key]

            str_one = str_two = False

            if s1[p1] == s3[p3]:
                str_one = check(s1, s2, s3, len_s1, len_s2, len_s3, p1+1, p2, p3+1)
            if s2[p2] == s3[p3]:
                str_two = check(s1, s2, s3, len_s1, len_s2, len_s3, p1, p2+1, p3+1)
            dict_map[key] = str_one or str_two
            return dict_map[key]
        if len(s3) != len(s1) + len(s2):
            return False
        return check(s1, s2, s3, len(s1), len(s2), len(s3), 0, 0, 0)

def main():
    obj = Solution()
    list_test = [["aabcc", "dbbca", "aadbbcbcac"], ["aabcc", "dbbca", "aadbbbaccc"], 
                 ["aabbcc", "aabbccc", "aabaabbcbcccc"]]
    
    for test in list_test:
        print(obj.isInterleave(test[0], test[1], test[2]), " = ", test)
if __name__ == "__main__":
    main()

# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.

 

# Example 1:


# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Example 2:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# Example 3:

# Input: s1 = "", s2 = "", s3 = ""
# Output: true
 

# Constraints:

# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1, s2, and s3 consist of lowercase English letters.
 

# Follow up: Could you solve it using only O(s2.length) additional memory space?