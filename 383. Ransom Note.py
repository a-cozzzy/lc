
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for letter in set(ransomNote):
            if magazine.count(letter) < ransomNote.count(letter):
                return False
        return True