class Solution:
  def longestCommonPrefix(self, strs):

    pre = ""
    i = 0
    
    if len(strs) == 0:
      return pre
    elif len(strs) == 1:
      pre += strs[0]
      return pre
    else:
      for i in range(min([len(x) for x in strs])):
        if [strs[x][i] for x in range(len(strs))].count(strs[0][i]) == len(strs):
          pre += strs[0][i]
          i += 1
        else:
          return pre
      return pre


result = Solution()
print(result.longestCommonPrefix(["flower", "flow", "flight"]))


