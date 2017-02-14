def uniquePaths(self, m, n):
        """
        :m x n matrix. Give all paths from top left to right bottom. Can only move left or down.
        :type m: int
        :type n: int
        :rtype: int
        """
        
        #if n > m: return uniquePaths(self, n, m)
        vars = [1] * m 
        
        for i in range(1, n):
            for j in range(1, m):
                vars[j] += vars[j - 1]
        return vars[m - 1]