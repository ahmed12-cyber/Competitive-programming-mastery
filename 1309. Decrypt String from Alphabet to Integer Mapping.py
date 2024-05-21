class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        def decrypt(str):
            return chr(int(str) + ord('a') - 1)
        
        arr = s.split('#')
        result = []
        
        for l in range(len(arr)):
            if arr[l] == "":
                continue
            i = 0
            if l == len(arr) - 1 and s[-1] != '#':
                while i < len(arr[l]):
                    result.append(decrypt(arr[l][i]))
                    i += 1
            elif len(arr[l]) > 2:
                while i < len(arr[l]) - 2:
                    result.append(decrypt(arr[l][i]))
                    i += 1
                result.append(decrypt(arr[l][i:i+2]))
            else:
                result.append(decrypt(arr[l]))
        
        return ''.join(result)

