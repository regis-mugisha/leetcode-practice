class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Create a frequency dictionaries for both strings
        str_s_freq = {}
        for char in s:
            str_s_freq[char] = str_s_freq.get(char, 0) + 1

        str_t_freq = {}
        for char in t:
            str_t_freq[char] = str_t_freq.get(char, 0) + 1

        # compare the frequency dictionaries
        if str_s_freq == str_t_freq:
            return True
        return False
        