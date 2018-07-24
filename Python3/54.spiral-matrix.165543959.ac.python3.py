class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
#         out_list = []
#         if not matrix or not matrix[0]:
#             return out_list
        
#         while True:
#             # Step 1: From left to right
#             out_list += matrix.pop(0) # add first row into output: matrix[0]
#             # Step 2: From top to bottom
#             if matrix: # whether is null
#                 for row in matrix:
#                     if row: # whether is null
#                         out_list.append(row.pop()) # add last one of each row when from top to bottom
#                     else:
#                         return out_list                
#             else: # return if matrix is null
#                 return out_list
#             # Step 3: From right to left
#             if matrix[-1]:
#                 out_list += matrix.pop()[::-1]
#             else:
#                 return out_list
            
#             # Step 4: Form bottom to up
#             if matrix:
#                 for row in matrix[::-1]:
#                     if row:
#                         out_list.append(row.pop(0))
#                     else:
#                         return out_list
#             else:
#                 return out_list
        
        # Use rotation idea
        
        if not matrix or not matrix[0]:
            return []
        out_list = [*matrix.pop(0)] #
        rotate_matrix = [*zip(*matrix)][::-1] # like transpose

        return  out_list + self.spiralOrder(rotate_matrix)
        