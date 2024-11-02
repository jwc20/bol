








"""
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]

(1,2,3)  (2,3,4) (1,3,4) (1,2,4)
Output: 4

"""



"""

input: is a list of integers where the values are greated than 0 and less than the length of input list


output: 
    - team of 3 soldiers where:
    -     (rating[i] < rating[j] < rating[k]) 
    -     or (rating[i] > rating[j] > rating[k]) 
    -     where (0 <= i < j < k < n).

        2,5,3,4,1
        
        take 2  => [2]
            check if next item is greater or lower

                5 is greater than 2, so the next item should also be greater.
                check 3,4,1 -> its not greater

            
        maybe have a namedtuple where we store boolean if its increasing or not, 

        - sliding window approach -> NO!

        - use stacks?

        push 2 -> [2]

        push 5 -> [2,5] , 
            - check if the first item in the stack is greater or lesser than the next item. 
            - stack.peek() < ratings[i] ?
            - if it is greater, then set a variable that it is increasing (e.g. is_increasing = True) 
            
        Since every items after 5 in the input list is not greater than 5, we pop the value from the stack and push the next item 3.

        push 3 -> [2,3]
            - is_increasing? => true
            - stack.peek() < ratings[i] ? => true
            - stack.push(rating[i])

        push 4 -> [2,3,4]
            - the size of this is 3, now we increment the count. => count = 1


"""


class Solution:
    def numTeams(self, rating: List[int]) -> int:

        count = 0
        stack = []

        
        



