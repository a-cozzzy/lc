class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        c_to_w = {}
        w_to_c = {}

        s_list = s.split()
        pattern = list(pattern)

        if len(s_list) != len(pattern):
            return False
        for char,word in zip(pattern,s_list):
            if char in c_to_w:
                if c_to_w[char]!=word:
                    return False
            else:
                c_to_w[char]=word

            if word in w_to_c:
                if w_to_c[word] != char:
                    return False
            else:
                w_to_c[word] = char
                
        return True 

