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
