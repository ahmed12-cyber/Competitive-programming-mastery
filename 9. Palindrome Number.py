class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Convert integer to string
        str_x = str(x)
        
        # Check if the string is equal to its reverse
        return str_x == str_x[::-1]


