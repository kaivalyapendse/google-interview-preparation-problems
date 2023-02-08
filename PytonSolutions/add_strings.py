#https://leetcode.com/problems/add-strings/description/

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(eval('{} + {}'.format(num1,num2)))
