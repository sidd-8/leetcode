class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Encode the representation
        dic = {'I': 1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}

        # Replace the 'subtracted' values
        s = s.replace('IV', 'IIII').replace('IX', 'VIIII').replace('XL', 'XXXX').replace('XC', 'LXXXX').replace('CD', 'CCCC').replace('CM', 'DCCCC')

        # Map each roman number to an int, and then sum
        return sum(map(lambda x: dic[x], s))