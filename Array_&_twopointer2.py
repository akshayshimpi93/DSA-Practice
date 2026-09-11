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
#     max_left = float('-inf')   # -inf ==== -♾️
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
#         if(ans == nums[i]):
#             freq += 1
#         else:
#             freq -= 1
#     return ans

# nums = [3,2,3]
# print(majorityElem(nums))
# --------------------------------------------------------------------------------
''' 26. GAS STATION '''
# gas = [1,2,4,5,9]    cost = [3,4,1,10,1]     Ouptu = 4

# def canCompleteCircle(gas,cost):

#     start = 0
#     tank = 0
#     total = 0

#     for i in range(len(gas)):
#         diff = gas[i] - cost[i]
#         total += diff
#         tank += diff

#         if tank < 0:
#             start = i+ 1
#             tank = 0

#     return start if total >= 0 else -1


# gas = [1,2,4,5,9] 
# cost = [3,4,1,10,1]
# print(canCompleteCircle(gas,cost))
# ------------------------------------------------------------------------------------------------------------------
''' 27 . SET MATRIX ZEROES'''

# def setZeros(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])

#     zero_rows = set()
#     zero_cols = set()

#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == 0:
#                 zero_rows.add(i)
#                 zero_cols.add(j)        # find row and column containing 0

#         #set row to 0
#         for i in zero_rows:
#             for j in range(cols):
#                 matrix[i][j] = 0


#         #set cols to 0
#         for j in zero_cols:
#             for i in range(rows):
#                 matrix[i][j] = 0

#     return matrix

# matrix = [[1,1,1],[1,0,1],[1,1,1]]
# print(setZeros(matrix))


''' OR ====='''
# def setZeroes( matrix):

#         m = len(matrix)
#         n = len(matrix[0])

#         row = [False] * m
#         col = [False] * n

#         # Mark
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     row[i] = True
#                     col[j] = True

#         # Update
#         for i in range(m):
#             for j in range(n):
#                 if row[i] or col[j]:
#                     matrix[i][j] = 0

#  matrix = [[1,1,1],[1,0,1],[1,1,1]]
# # print(setZeros(matrix))

# ---------------------------------------------------------------------------------------------
''' Spiral matrix'''
#Input = [[1,2,3],[4,5,6],[7,8,9]]
# output = [1,2,3,6,9,8,7,4,5] 
# def Spiralmatrix(matrix):
#     m = len(matrix)
#     n = len(matrix[0])

#     srow = 0
#     scol = 0
#     erow = m - 1
#     ecol = n - 1

#     answer = []

#     while srow <= erow and scol <= ecol:

#         # Top
#         for j in range(scol, ecol + 1):
#             answer.append(matrix[srow][j])

#         # Right
#         for i in range(srow + 1, erow + 1):
#             answer.append(matrix[i][ecol])

#         # Bottom
#         for j in range(ecol - 1, scol - 1, -1):
#             if srow == erow:
#                 break
#             answer.append(matrix[erow][j])

#         # Left
#         for i in range(erow - 1, srow, -1):
#             if scol == ecol:
#                 break
#             answer.append(matrix[i][scol])

#         srow += 1
#         erow -= 1
#         scol += 1
#         ecol -= 1

#     return answer


# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# print(Spiralmatrix(matrix))
# ----------------------------------------------------------------------------------------------------
'''27.Rotate image'''
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# def rotateimage(matrix):
#     n = len(matrix)

#     for i in range(n):   # transpose
#         for j in range(i+1,n):
#             matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]


#     for row in matrix:   # rotate
#         row.reverse()


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# rotateimage(matrix)
# print(matrix)             #time = O(n^2)   and space = O(1)
# ---------------------------------------------------------------------------------------------------------