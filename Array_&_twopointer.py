# 1) TWO POINTER PROBLEM 
# EXAMPLE =  nums = [2,7,11,15] , target = 9    output = [0,1] ====== solving by Optiomize way

''' optimize way '''
# def twosum(nums,target):
#     seen = {}           # hashmap(c++)  , dictionary(python)
#     for i , num in enumerate(nums):             # here i is {index} and num is {value} in hashmap & dictionary
#         complement = target - num               # we use enumerated to solve this problem in optimize way enumerate(index,value)
#         if complement in seen:
#             return [seen[complement],i]
#         seen[num] = i
#     return []

# nums = [2,7,11,15]
# target = 9                                            # Time  & space complexity = O(n)
# print(twosum(nums,target)) 

''' brute force '''
# def twosum(nums,target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1,n):
#             if nums[i] + nums[j] == target:
#                 return[i, j]
#         return []

# nums = [2,7,11,15]
# target = 9
# print(twosum(nums,target))    # output = [0,1]        # Time - O(n^2)  & Space - O(1) 
# -------------------------------------------------------------------------------------------------------------------

## find missing and repeted value  Output = [9,5]  

### BETTER WAY
# def FindMissingAndRepetedValue(grid):
#     n = len(grid)
#     count = [0] * (n*n+1)

#     for row in grid:
#         for num in row:
#             count[num] += 1

#         repeted = missing = -1
#         for num in range(1, n*n+1):
#             if count[num] == 2:
#                 repeted = num

#             elif count[num] == 0:
#                 missing = num

#         return [repeted,missing]



# grid = [[9,1,7],[8,9,2],[3,4,6]]
# print(FindMissingAndRepetedValue(grid))       # Time = O(n^2)  & Space = O(n^2)
# ------------------------------------------------------------------------------------------------

'''3) 121. Best time to buy and sell the stock '''
## Example : price = [7,1,5,3,6,4]  ,  output = 5

# def max_profit(prices):
#     min_price = float('inf')
#     max_profit = 0

#     for price in prices:
#         if price < min_price:
#             min_price = price
#         elif price - min_price > max_profit:
#             max_profit = price - min_price
#     return max_profit

# prices = [7,1,5,3,6,4]
# print(max_profit(prices))           # time = O(n)   &  space = O(1)
# -------------------------------------------------------------------------------------------------

# 4) 217. Contain duplicate
## input = [1,2,3,1]     output = True or false

# def containDuplicate(nums):
#     seen = set()

#     for num in nums:
#         return True
#     seen.add(num)

#     return False

# nums = [1,2,3,1]
# print(containDuplicate(nums))           #Time = O(n)   & Space = O(n)


### optimize 
# def containDuplicate(nums):                 # nums = [4,3,2,7,3]
#     nums.sort()                             # sorted nums = [2,3,3,4,7]
#     for i in range(1,len(nums)):
#         if nums[i] == nums[i-1]:            # comapre = current[i] == previous[i-1]  >>>> current[3] === previous[3]
#             return True
#     return False

# nums = [4,3,2,7,3]
# print(containDuplicate(nums))               ## Time == O(n log n) and space = O(1)
# ------------------------------------------------------------------------------------------------------------------------------
''' 4). (238)  product of array except self:'''
#  Input = [1,2,3,4]     output = [24,12,8,6]

# def productExceptself(nums):
#     n = len(nums)
#     result = [1] * n

# # left pass = result[i] = product of all element before i
#     prefix = 1
#     for i in range(n):
#         result[i] = prefix
#         prefix *= nums[i]

# # right pass = multiply by product of all element after i 
#     suffix = 1
#     for i in range(n-1,-1,-1):
#         result[i] *= suffix
#         suffix *= nums[i]

#     return result 

# nums = [1,2,3,4] 
# print(productExceptself(nums))            ## Time = O(n)  & space = O(1)
# -----------------------------------------------------------------------------------------------------------------------------------
'''5). (53) Maximum subarray(kadana's) '''
## Input = [4,-1,2,1]
## Input2 = [-2,1,-3,4,-1,2,1,-5,4]  output = 6


# def maximumsubarray(nums):
#     max_ending_here = max_so_far = nums[0]

#     for i in nums[1:]:
#         max_ending_here = max(i , max_ending_here + i)

#         max_so_far = max(max_ending_here,max_so_far)

#     return max_so_far


# nums = [4,-1,2,1]
# print(maximumsubarray(nums))          # time = O(n)  & space = O(1)
# --------------------------------------------------------------------------------------------------------------------------------
