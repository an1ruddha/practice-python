from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        input_list = words.copy()
        result = [0]
        for _ in range(len(input_list)-1):
            match_word = input_list.pop()
            for word in input_list:
                match_flag = False
                for match_char in match_word:
                    if match_char in word:
                        match_flag = True
                        break
                if not match_flag:
                    result.append(len(word)*len(match_word))
        return max(result)

def main():
    obj = Solution()
    list_words = [["abcw","baz","foo","bar","xtfn","abcdef"],
                  ["a","ab","abc","d","cd","bcd","abcd"],
                  ["a","aa","aaa","aaaa"]]
    
    for words in list_words:
        print(obj.maxProduct(words), " = ", words)
if __name__ == "__main__":
    main()
    # Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

    # Example 1:

    # Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    # Output: 16
    # Explanation: The two words can be "abcw", "xtfn".
    # Example 2:

    # Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
    # Output: 4
    # Explanation: The two words can be "ab", "cd".
    # Example 3:

    # Input: words = ["a","aa","aaa","aaaa"]
    # Output: 0
    # Explanation: No such pair of words.
