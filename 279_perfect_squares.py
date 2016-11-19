#279. Perfect Squares My Submissions Question
#Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

#For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

#Credits:
#Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

class Solution(object):
    numSquaresDP = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if len(self.numSquaresDP) <= n:
            squares = [v**2 for v in xrange(1, int(n**0.5)+1)]
            for i in xrange(len(self.numSquaresDP), n + 1):
                self.numSquaresDP.append(min(1 + self.numSquaresDP[i-x] for x in squares[:int(i**0.5)]))
        return self.numSquaresDP[n]
