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

