#127. Word Ladder My Submissions Question
#Total Accepted: 66286 Total Submissions: 338706 Difficulty: Medium
#Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

#Only one letter can be changed at a time
#Each intermediate word must exist in the word list
#For example,

#Given:
#beginWord = "hit"
#endWord = "cog"
#wordList = ["hot","dot","dog","lot","log"]
#As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#return its length 5.

#Note:
#Return 0 if there is no such transformation sequence.
#All words have the same length.
#All words contain only lowercase alphabetic characters.

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        Bidirectional BFS to beat the time limit
        """
        fronts = [{beginWord}, {endWord}]
        levels = [1, 1]
        while fronts[0] and fronts[1]:
            if len(fronts[0]) > len(fronts[1]):
                fronts.reverse()
                levels.reverse()
            newLevel = set()
            for word in fronts[0]:
                for i in xrange(len(beginWord)):
                    for char in string.lowercase:
                        newWord = word[:i] + char + word[i + 1:]
                        if newWord in fronts[1]:
                            return levels[0] + levels[1]
                        if newWord in wordList:
                            newLevel.add(newWord)
                            wordList.remove(newWord)
            fronts[0] = newLevel
            levels[0] += 1
        return 0
