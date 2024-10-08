
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
#print(checker(word1, word2))


def longestCommonPrefix(strs) -> str:
        lcp = strs[0]
        last_common = ""
        for i in range(len(strs) - 1):
            lcp = checker(lcp, strs[i + 1])
            if lcp == "":
                return lcp

        if len(strs) == 1:
            return strs[0]

        return lcp


# 134. Gas Station

gas = [4,5,3,1,4]
cost = [5,4,3,4,2]

# gas = [1,2,3,4,5]
# cost = [3,4,5,1,2]

# gas = [2,3,4]
# cost = [3,4,3]

def reconstruct_list(sp, gas, cost):
    gas1 = gas[sp:]
    gas2 = gas[:sp]
    cost1 = cost[sp:]
    cost2 = cost[:sp]

    return (gas1 + gas2), (cost1 + cost2)

def try_circuit(sp, gas, cost):
    new_lists = reconstruct_list(sp, gas, cost)
    gas = new_lists[0]
    cost = new_lists[1]
    print(gas, cost)

    current = gas[0]
    for i in range(len(gas) - 1):
        print(i, "----")
        if current - cost[i] > 0:
            current = current - cost[i] + gas[i + 1]
            print(current)
        else:
            current = -1
            return current
    if current - cost[-1] < 0:
        return -1
    return current

def canCompleteCircuit(gas, cost) -> int:
    
    for i in range(len(gas)):
        if gas[i] > cost[i]:
            if try_circuit(i, gas, cost) > 0:
                return i
    return -1 

#print(canCompleteCircuit(gas, cost))


#392. Is Subsequence

# s = "abc"
# t = "ahbgdc"

s = "b"
t ="abc"

x = ""

#print(list(x))

def isSubsequence(s: str, t: str) -> bool:
    s = list(s)
    t = list(t)

    if len(s) == 0:
        return False

    while len(t) > 0:
        if t[-1] != s[-1]:
            t.pop()
        elif t[-1] == s[-1]:
            t.pop()
            s.pop()
        if len(s) == 0:
            return True
    return False

#print(isSubsequence(s, t))


#28. Find the Index of the First Occurrence in a String

haystack = "sadbutsad"
needle = "sad"
gt = len(haystack)
counter =  0


#print(haystack[:len(needle)])

def compare_words(haystack, needle, counter):
    if haystack[:len(needle)] == needle:
        return counter
    elif counter > gt:
        return -1
    counter += 1
    return compare_words(haystack[1:], needle, counter)

def strStr(haystack: str, needle: str) -> int:
    position = 0
    while True:
        None

#print(compare_words(haystack, needle, counter))
# if True:
#     print("s")
# for i in range(5, -1, -1):
#     print(i)


# 209 Minimun sub array sum

def minSubArrayLen(target, nums) -> int:
        l, total = 0, 0
        min_sa = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_sa = min(r - l + 1, min_sa)
                total -= nums[l]
                l += 1
        
        return 0 if min_sa == float("inf") else min_sa

list_test = [1, 2, 3, 4, 5]
list_test.pop(0)

#print(list_test)

s = "aab"

#3. Longest Substring wihtout Repeating characters

# def lengthOfLongestSubstring(s: str) -> int:
#     normal_s = s
#     memory = set()
#     s = list(s)
#     lls = 0

#     for i in range(len(normal_s)):
#         print(i)
#         if normal_s[i] not in memory:
#             memory.add(normal_s[i])
#         else:
#             lls = max(lls, len(memory))
#             s = s[i:]
#             memory = set()
#             memory.add(normal_s[i])
            
#         print(s, memory, lls)

#     return lls

def lengthOfLongestSubstring(s: str) -> int:

    memory = set()
    l = 0
    lls = 0
    for r in range(len(s)):
        while s[r] in memory:
            memory.remove(s[l])
            l += 1
        memory.add(s[r])
        lls = max(lls, r - l + 1)
    
    return lls

#print(lengthOfLongestSubstring(s))

arr_test = [1, 2, 7, 12, 34, 76, 89, 112, 113, 134]

# def binarySearchTest(arr, target): # Decent but im not using O(1) memory

#     l, r = 0, len(arr) - 1
#     mid = len(arr)//2
#     while l < r:
#         print(arr, mid)
#         if target == arr[mid]:
#             return True
#         elif target > arr[mid]:
#             arr = arr[mid:]
#         else:
#             arr = arr[:mid]

#         r = len(arr) - 1
#         mid = len(arr)//2
#     return False

def binarySearchTest(arr, target): # Now using O(1) memory

    l, r = 0, len(arr) - 1
    mid = 0
    while l <= r:
        mid = (r + l)//2
        print(mid, l, r)

        if target > arr[mid]:
            #arr = arr[mid:]
            l = mid + 1
        elif target < arr[mid]:
            #arr = arr[:mid]
            r = mid - 1
        else:
            return True
        
    return False

#35. Search Insert Position

#print(binarySearchTest(arr_test, 13))

# def checker()

def searchInsert(nums, target):
    
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r)//2

        if target > nums[mid]:
            l = mid + 1
        elif target < nums[mid]:
            r = mid - 1
        elif target == nums[mid]:
            return mid
    return l
        
#print(searchInsert(arr_test, 180))

nums = [0, 0, 1, 1, 1, 1, 2 ,3, 3, 3, 4, 7, 7, 8, 9] 
#[0,0,1,1,1,2,2,3,3,4]

# def removeDuplicates(nums) -> int: This wont work because of the indexsss
#     memory = set()
#     for i in range(len(nums)):
#         print(nums, i, nums[i])
#         if nums[i] not in memory:
#             memory.add(nums[i])
#         else:
#             nums.pop(i)
#             nums.append("_")
#     return len(memory)

# def removeDuplicates(nums) -> int:
#     memory = set()
#     l = 0
#     while l < len(nums):
#         print(memory, nums, l, nums[l])
#         if nums[l] not in memory:
#             memory.add(nums[l])
#             nums.append("_")
#             l += 1
#         elif nums[l] == "_":
#             break
#         else:
#             nums.pop(l)
#             nums.append("_")
#     return len(memory) - 1

def removeDuplicates(nums) -> int:
    l = 1
    for r in range(1, len(nums)):
        print(nums)
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1
    #print(nums)
    return l

#print(removeDuplicates(nums))

nums = [1, 2, 3, 0, 0, 4, 5, 6, 0, 7, 0, 0, 0, 2]

def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    starter = True
    l = 0
    for r in range(len(nums)):
        if starter:
            if nums[r] == 0:
                starter = False
                l = r
        elif nums[r] != 0:
            nums[l] = nums[r]
            nums[r] = 0
            l += 1
    print(nums)

#print(moveZeroes(nums))

def removeDuplicatesII(nums) -> int:
    l, r = 0, 0

    while r < len(nums):
        count = 1
        while r + 1 < len(nums) and nums[r] == nums[r + 1]:
            r += 1
            count += 1
        
        for i in range(min(2, count)):
            nums[l] = nums[r]
            l += 1
        r += 1
    return l

#181 Rotate Array FLAWEDDDDDD solution

# def rotate(nums, k: int) -> None:
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     if len(nums) == 1:
#         return nums
#     l = 0
#     for r in range(len(nums) - k, len(nums)):
#         memory = nums[l]
#         nums[l] = nums[r]
#         nums[r] = memory
#         l += 1
#     if len(nums)%2 != 0:
#         value = nums[len(nums)-k -1]
#         nums.pop(len(nums) - k-1)
#         nums.append(value)

# The following is the right solution for O(1) time complexity
def rotate(nums, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    def rev(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1
            r -=1

    rev(0, len(nums) - 1)
    rev(0, k-1)
    rev(k, len(nums)-1)
    return nums


#print(5%10)

# FROM 1d to 2d

def construct2DArray(original, m, n):
    
    if len(original) != n*m:
        return []

    res = []
    checker = 0
    data = []
    for i in range(len(original)):
        data.append(original[i])
        checker += 1
        if checker == n:
            res.append(data)
            data = []
            checker = 0
    
    return res

#print(100%6)

#print(ord('b') - ord('a') + 1)

def dfs(graph, Node):

    stack = []



root = [3,9,20,0,0,15,7]

def averageOfLevels(root):
    l, itera = 0, 0
    avgs = []
    n = 0
    while n <= len(root):
        n += 2**itera
        avg = 0
        if n > len(root):
            return avgs
        print(l, n)
        for i in range(l, n):
            avg += root[i]
        
        avgs.append(avg)
        l = n
        itera += 1
    return avgs

print(averageOfLevels(root))