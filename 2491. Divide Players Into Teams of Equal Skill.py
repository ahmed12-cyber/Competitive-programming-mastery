class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()
        n = len(skill)
        t = skill[0] + skill[-1]
        ans = 0
        i, j = 0, n - 1
        while i < j:
            if skill[i] + skill[j] != t:
                return -1
            ans += skill[i] * skill[j]
            i += 1
            j -= 1
        return ans
