class Solution:
    """Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    """
    @staticmethod
    def two_sum(nums, target):
        """

        Args:
            nums: int[] - an array of integers
            target: int - a target integer

        Returns: int[] - integer array with the index positions of the array elements to sum
        """
        # can assume exactly one solution - otherwise would implement checks on length first, as well as have exit criteria for no solution.

        prev_integers = {}
        for i, n in enumerate(nums):
            remainder = target - n
            if remainder in prev_integers:
                # we have a solution! Obtain the index
                remainder_ix = prev_integers[remainder]
                return [i, remainder_ix]
            else:
                # store the element and ix
                prev_integers[n] = i
