"""
https://leetcode.com/problems/sort-the-people/description/?envType=daily-question&envId=2024-07-22

2418. Sort the People
Easy

You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.
Return names sorted in descending order by the people's heights.



Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.
Example 2:

Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.


Constraints:

n == names.length == heights.length
1 <= n <= 103
1 <= names[i].length <= 20
1 <= heights[i] <= 105
names[i] consists of lower and upper case English letters.
All the values of heights are distinct.
"""

from typing import List
from collections import namedtuple


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        """
        we can use dictionary to set key, value pairs with the items from the names and heights lists.
        This will cost O(n) where n is the length of the names/heights list.

        Since we are using python, we can use namedTuples, which will be more memory efficient than dictionary since we are not storing the keys.
        namedTuples are also immutable which makes it more appropriate for this problem (the heights doesn't change for the person).

        """

        Person = namedtuple("Person", ["name", "height"])

        combined = zip(names, heights)
        people = [Person(name, height) for name, height in combined]

        people_sorted = sorted(people, key=lambda person: person.height, reverse=True)

        return [person.name for person in people_sorted]


print(Solution().sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))
print(Solution().sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150]))
print(
    Solution().sortPeople(
        [
            "IEO",
            "Sgizfdfrims",
            "QTASHKQ",
            "Vk",
            "RPJOFYZUBFSIYp",
            "EPCFFt",
            "VOYGWWNCf",
            "WSpmqvb",
        ],
        [17233, 32521, 14087, 42738, 46669, 65662, 43204, 8224],
    )
)
