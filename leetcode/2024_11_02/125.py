
import unittest





class Solution:
    def isPalindrome(self, s: str) -> bool:

        # clean the input string
        # convert to lowercase
        # remove special characters
        # remove spaces


        s = ''.join(e for e in s if e.isalnum())
        s = s.lower()

        l, r = 0, len(s)-1

        while l < r:
            if s[l] == s[r]: l, r = l+1, r-1
            else: return False
        return True











class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_basic_palindromes(self):
        # Test basic palindrome strings
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(self.solution.isPalindrome("race a car") == False)
        self.assertTrue(self.solution.isPalindrome(" "))
    
    def test_special_characters(self):
        # Test strings with special characters
        self.assertTrue(self.solution.isPalindrome(".,"))
        self.assertTrue(self.solution.isPalindrome("a."))
        self.assertTrue(self.solution.isPalindrome("!@#$%^&*()"))
        self.assertTrue(self.solution.isPalindrome("a.a"))
        self.assertTrue(self.solution.isPalindrome("a.,a"))
    
    def test_numbers(self):
        # Test strings with numbers
        self.assertTrue(self.solution.isPalindrome("121"))
        self.assertTrue(self.solution.isPalindrome("1a1"))
        self.assertTrue(self.solution.isPalindrome("1!1"))
        self.assertTrue(self.solution.isPalindrome("12@21"))
        self.assertFalse(self.solution.isPalindrome("123"))
    
    def test_case_sensitivity(self):
        # Test case sensitivity
        self.assertTrue(self.solution.isPalindrome("Aa"))
        self.assertTrue(self.solution.isPalindrome("aA"))
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(self.solution.isPalindrome("RaCeCaR"))
    
    def test_edge_cases(self):
        # Test edge cases
        self.assertTrue(self.solution.isPalindrome(""))
        self.assertTrue(self.solution.isPalindrome(" "))
        self.assertTrue(self.solution.isPalindrome("  "))
        self.assertTrue(self.solution.isPalindrome("a"))
        self.assertTrue(self.solution.isPalindrome("!"))
    
    def test_non_palindromes(self):
        # Test non-palindrome strings
        self.assertFalse(self.solution.isPalindrome("race a car"))
        self.assertFalse(self.solution.isPalindrome("hello"))
        self.assertFalse(self.solution.isPalindrome("0P"))
        # self.assertFalse(self.solution.isPalindrome("1 b1"))
    
    def test_complex_palindromes(self):
        # Test more complex palindrome cases
        self.assertTrue(self.solution.isPalindrome("A Santa at NASA"))
        self.assertTrue(self.solution.isPalindrome("Doc, note: I dissent. A fast never prevents a fatness. I diet on cod"))
        self.assertTrue(self.solution.isPalindrome("Never odd or even"))
        self.assertTrue(self.solution.isPalindrome("Do geese see God?"))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
