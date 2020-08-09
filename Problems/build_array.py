# Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

# Build the target array using the following operations:

# Push: Read a new element from the beginning list, and push it in the array.
# Pop: delete the last element of the array.
# If the target array is already built, stop reading more elements.
# You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.

# Return the operations to build the target array.

# You are guaranteed that the answer is unique.
# Source - https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        target_idx, cur_read_num = 0, 1

        stack_operation = []

        while target_idx < len(target):

            # Push current read number
            stack_operation.append('Push')

            if target[target_idx] == cur_read_num:
                # Current read number is what we need, keep it and update target index
                target_idx += 1

            else:
                # Pop out unnecessary element
                stack_operation.append('Pop')

            # current read number always +1 after each iteration
            cur_read_num += 1

        return stack_operation