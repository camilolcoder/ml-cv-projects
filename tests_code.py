
#test_list = [6,1,3,2,4,7]
test_list = [7,1,5,3,6,4]
#[3, 8, 2, 4, 11, 1, 2, 12]
#[2,7,1,4,11]

# [3, 8, 2, 4, 11, 1, 2, 12]

# LeetCode 121 - First aproach the error was focusing on the difference instead of the numbers

# def maxProfit(prices) -> int:
#     #Worst escenario the prices keep descending
#     #Best they keep ascendint (Hence I need to keep the first value)
#     #[4, 3, 2, 4, 1, 8, 7]
#     #
#     best_profit = 0
#     low_baller = 1000000
#     even_lower = 1000000
#     for i in range(len(prices) - 1):

#         actual_value = prices[i+1] - prices[i]
#         new_value = prices[i+1] - low_baller
#         new_lower = prices[i]
#         if new_lower < even_lower:
#             even_lower = new_lower
#         print(actual_value, new_value, low_baller, even_lower)
#         if new_value >= best_profit:
#             best_profit = new_value
#         if actual_value >= best_profit:
#             low_baller = prices[i]
#             best_profit = actual_value
        
#     return best_profit

def maxProfit(prices) -> int:
    #aproach with to pointers
    l, r = 0, 1
    max_profit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        r += 1

    return max_profit 

# 122 Leetcode - best time to sell stocks 2 

def maxProfit2(prices) -> int:
    #aproach with to pointers
    l, r = 0, 1
    total_profit = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            if profit > 0:
                l = r
                total_profit += profit
        else:
            l = r
        r += 1

        
    return total_profit 


#print(maxProfit2(test_list))

#Jump Game 55

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
test_list = [2,3,1,1,4]

def canJump(nums) -> bool:
    goal = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    
    return True if goal == 0 else False

#print(canJump(test_list))

# 14. Longest Common Prefix
# O(n)^2

def checker(word1, word2):
    prefix = ""
    tester = word1
    if len(word1) > len(word2):
        tester = word2
    for i in range(len(tester)):
        if word1[i] != word2[i]:
            return prefix
        else:
            prefix += tester[i]
    return prefix

word1 = "reflower"
word2 = "flow"
print(checker(word1, word2))


def longestCommonPrefix(strs) -> str:
        lcp = strs[0]
        last_common = ""
        for i in range(len(strs) - 1):
            lcp = self.checker(lcp, strs[i + 1])
            if lcp == "":
                return lcp

        if len(strs) == 1:
            return strs[0]

        return lcp

