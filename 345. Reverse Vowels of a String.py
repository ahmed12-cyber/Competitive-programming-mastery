class Solution:
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')
        cs = list(s)
        i, j = 0, len(cs) - 1
        while i < j:
            while i < j and cs[i] not in vowels:
                i += 1
            while i < j and cs[j] not in vowels:
                j -= 1
            if i < j:
                cs[i], cs[j] = cs[j], cs[i]
                i += 1
                j -= 1
        return ''.join(cs)
