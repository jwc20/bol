class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        """
        Inputs: integer n, array rounds
        Output: sorted array

        Constraints:
        circular track consisting of 1-n sectors.
        m = length of rounds?
        ith round starts at rounds[i-1] and ends at rounds[1]

        EX1: n = 4, rounds=[1,3,1,2]

        round1 = [1,2,3]
        round2 = [4,1]
        round3 = [2]

        We probably have to use linked list.

        The Naive approach would be to use a hashmap to store the count for all the sectors visited.
        So for example 1
        d = {1:2, 2:2, 3:1, 4:1}
        Then append the most visited into an array.
        (Does most visited mean visited more than once?)
        We need to count the numbers in between the rounds. Ex1: [1,3] => [1,2,3]
        This will take up O(n) space.

        Another approach would be to dynamically resize the input array by n and count from there.
        (Amortized)

        Another approach would be to use two pointers, where the value at the next index is greater         than the current index, then we need to count the numbers between.
        If the next value is greater, then we need to iterate the number up to n and count those           numbers.
        O(n) time and space.

        How can I reduce the space to O(1)?
            Use the existing input array?

        [1,3,1,2]  => [1,2,3,4,1,2]

        Append the numbers in between rounds at the end of the array.
        [1,3,1,2,2,4]
        count the max and swap positions if the value count matches the max, then return the sliced list.

        n = 7, rounds = [1,3,5,7] => [1,2,3,4,5,6,7]
        then max_count = 1, so return all.


        31 min

        edge cases,
        """

        current = 0
        next = 1

        for i in range(len(rounds)):
            if rounds[next] - rounds[current] > 1:  # and not 0
                for j in range(rounds[current] + 1, rounds[next]):
                    num = rounds[current]
                    num += 1
                    rounds.append(num)
                    print(rounds)
                current += 1
                next += 1
            # elif rounds
