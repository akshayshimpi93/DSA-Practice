'''💥🥇 SLIFING WINDOW '''
'''Slinding Window Maximum '''
#input =  [1,3,-1,-3,5,3,6,7], k = 3 
#output = [3,3,5,5,6,7]

# from collections import deque

# def max_sliding_window(nums, k):
#     dq = deque()
#     result = []

#     for i in range(len(nums)):

#         # Remove indices outside the window
#         while dq and dq[0] <= i - k:
#             dq.popleft()

#         # Remove smaller elements from the back
#         while dq and nums[dq[-1]] <= nums[i]:
#             dq.pop()

#         # Add current index
#         dq.append(i)

#         # Start adding maximums after first window
#         if i >= k - 1:
#             result.append(nums[dq[0]])

#     return result


# nums = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3

# print(max_sliding_window(nums, k))
# -------------------------------------------------------------------------------------------
''' 122.Best time to buy and sell the stock'''
# input = [7,1,5,3,6,4]
# output = 7

# def buy_sell_stock(price):
#     max_profit = 0
#     for i in range(len(price)-1):
#         if price[i] < price[i+1]:
#             max_profit += price[i+1] - price[i]

#     return max_profit

# price = [7,1,5,3,6,4]
# print(buy_sell_stock(price))
# -------------------------------------------------------------------------
''' Longest substring without repeting character '''
# Input: s = "abcabcbb"
# Output: 3

# def longest_substring(s):
#     seen = {}   #char = last index seen
#     left = 0
#     longest = 0

#     for right,char in enumerate(s):
#         if char in seen and seen[char] >= left:
#             left = seen[char] + 1   # move left past the duplicate
#         seen[char] = right
#         longest = max(longest , right - left + 1)
#     return longest

# s = "abcabcbb"
# print(longest_substring(s))
# -------------------------------------------------------------------------------------------------------
''''37) Longest repeating character replacement '''
#input = s = "ABAB" , k = 2
#output = 4

def characterReplacement(s,k):
    count = {}
    max_count = 0 #count of the most frequent char in current window
    left = 0
    result = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right],0) + 1
        max_count = max(max_count,count[s[right]])

        # window size - max_count = char needing replacement

        if (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1

        result = max(result,right - left + 1)

    return result 

s =  "ABAB"
k = 2
print(characterReplacement(s,k))