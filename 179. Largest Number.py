class Solution(object):
    def largestNumber(self, nums):
        from functools import cmp_to_key

        vs = [str(v) for v in nums]
        vs.sort(key=cmp_to_key(lambda a, b: (b + a > a + b) - (b + a < a + b)))
        if vs[0] == "0":
            return "0"
        return "".join(vs)
