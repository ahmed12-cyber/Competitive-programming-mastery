class Solution(object):
    def interpret(self, c):
        """
        :type c: str
        :rtype: str
        """
        A = []
        A.append(c[0])
        
        for s in range(1, len(c)):
            if c[s] == ')':
                if A and A[-1] == '(':
                    A.pop()
                    A.append('o')
            elif c[s] == '(':
                A.append(c[s])
            elif c[s] == 'G' or c[s] == 'a' or c[s] == 'l':
                if A and A[-1] == '(':
                    A.pop()
                    A.append(c[s])
                else:
                    A.append(c[s])
        
        return ''.join(A)


