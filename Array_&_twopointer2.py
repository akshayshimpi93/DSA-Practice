'''1)167 TWO SUM ll - Input array is sorted'''
# Input = [2,7,11,15],target = 9
#output = [1,2]

# def twoSumll(nums,target):
#     i = 0
#     j = len(nums) - 1


#     while i < j:
#         if nums[i] + nums[j] < target :
#             i += 1
#         elif nums[i] + nums[j] > target:
#             j -= 1
#         else:
#             return i+1, j+1
        
#     return -1

# nums = [2,7,11,15]
# target = 9
# print(twoSumll(nums,target))      # time = O(n)  and Space = O(1)
# -------------------------------------------------------------------------------------
'''2) Valid palindrome'''
#input = s = "A man , a plan , a canal : panama"
#output = true

# def validpalidrom(sen):
#   st = 0
#   end = len(sen) - 1

#   while(st < end):
#     # skip non - alphanumeric chars
#     while st < end and not sen[st].isalnum():
#       st += 1
#     while st < end and not sen[end].isalnum():
#         end -= 1
#     if sen[st].lower() != sen[end].lower():
#        return False
#     st += 1
#     end -= 1

#   return True 

# sen = "A man , a plan , a canal : panama"
# print(validpalidrom(sen))     # time = O(n)  & space = O(1)
#--------------------------------------------------------------------------------------------
'''25.maximum valid sum '''
#Input: nums = [1,3,5,2,8], k = 2
# Output: 13

# def maxvalidsum(nums,k):
#     n = len(nums)
#     best = float('-inf')
#     max_left = float('-inf')
#     i = 0

#     for j in range(k,n):
#         while i <= j - k:
#             max_left = max(max_left, nums[i])
#             i += 1
#         best = max(best,max_left + nums[j])
#     return best

# nums = [1,3,5,2,8]
# k = 2
# print(maxvalidsum(nums,k))
# ------------------------------------------------------------------------------------------------
''' Majority Element '''
#input= [3,2,3]
# output = 3

# def majorityElem(nums):
#     freq = 0
#     ans = 0
#     n = len(nums)

#     for i in range(n):
#         if(freq == 0):
#             ans = nums[i]
#             if(ans == nums[i]):
#                 freq += 1
#             else:
#                 freq -= 1
#     return ans

# nums = [3,2,3]
# print(majorityElem(nums))
# -------------------------------------------------------