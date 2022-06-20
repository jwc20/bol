class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        SET lower, current, and upper = 0 (indices) 
        WHILE the current index is greater than the upper index
            IF the element in the current index of the list is less than the element in the upper index,
                nums[c] == nums[u]
                RETURN true
            ELSE 
                INCREMENT current
        return False

        """

        l = 0
        u = len(nums) - 1
        c = 0

        while c < u:
            if nums[c] == nums[u]:
                return True
            else:
                c += 1

        return False



a = [1,2,3,1]
# => true

b = [1,2,3,4]
# => false

c = [1,1,1,3,3,4,3,2,4,2]
# => true

print(Solution.containsDuplicate(a))
