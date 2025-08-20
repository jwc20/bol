class Solution:
    def maxScore(self, s: str) -> int:

        """
        s is an element of {0,1}

        input: string s
        output: int score

        split s into two substring, left and right

        "011101"

        l=0, r=11101 => 1+4

        --------

        an array problem.
        O(n) time => traverse the string (array) once and get the solution

        not sure if there is O(1) space sol'n. we might have to use dictionary, set, tuples,...

        so what is the most naive sol'n???
            traverse the string, with the

            011101
            - we want to have an index starting at left_end=0 and increment to mark the end position of the left substring.
            - when we reach left_end, count the score.
            - store the score in a dictionary or namedtuple
                - dictionary with key as left_end and value as score

        [0], [11101] =>  [[0: 5]]
        [01], [1101] => [[0: 5], [1:4]], ...

        O(n) time and space where n is the length of the string
        """

        result = []
        left_end = 0
        left_score = 0
        right_score = 0

        # convert the string to array
        # s_arr = s.split()
        # split the s string into a array of chars
        s_arr = [char for char in s]
        print(s_arr)

        while left_end < len(s):
            # count scores here
            if s_arr[left_end] == '0':
                left_score += 1 

            result.append(s_arr[left_end], score])
            left_end+=1

        return -1

# run the solution
solution = Solution()
print(solution.maxScore("011101"))
