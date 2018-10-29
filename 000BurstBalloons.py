# 312. Burst Balloons

# Google Tag

'''
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''

class Solution:

    # Time Limit Exceeded.
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def dfs(arr, i):

            if len(arr) ==  1 and i == 0:
                return arr[0]
        
            left = arr[i - 1] if i > 0 else 1
            right = arr[i + 1] if i + 1 < len(arr) else 1
            res = arr[i] * left * right
            
            new = [v for v in arr]
            new.pop(i)
            
            m_n = 0
            for j in range(len(new)):
                t_m = dfs(new, j)
                if t_m > m_n:
                    m_n = t_m
                
            return res + m_n

        m = 0
        for ni in range(len(nums)):
            t_m = dfs(nums, ni)
            if t_m > m:
                m = t_m

        return m

    '''
    1. DFS + Dictionary to record caldulated ones
    '''
    # Time Limit Exceeded
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        
        def dfs(nums):
            
            if tuple(nums) in d:
                return
            
            m = 0
            for i in range(len(nums)):
                left = nums[i - 1] if i - 1 >= 0 else 1
                right = nums[i + 1] if i + 1 < len(nums) else 1
                l = [v for v in nums]
                l.pop(i)
                if tuple(l) not in d:
                    dfs(l)
                    
                res = left * nums[i] * right + d[tuple(l)]
                if res > m:
                    m = res
                    
            d[tuple(nums)] = m
            return
        
        dfs(nums)
        
        return d[tuple(nums)] 

    '''
    DP, O(n^3)
    Huahua Youtube link: https://www.youtube.com/watch?v=z3hu2Be92UA

    Find the k to maximize the score.
    The k divides the problem into two sub problems.
            ------------     ------------
     i - 1 |            | k |            | j + 1
            ------------     ------------

    c[i][j] = maxCoins(nums[i] ~ nums[j])
    ans = c[1][n]
    c[i][j] = max(c[i][k - 1] + nums[i - 1]*nums[k]*nums[j + 1] + c[k + 1][j] | i <= k <= j)
    '''

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        
        c = [[0 for i in range(n + 2)] for j in range(n + 2)]
        nums = [1] + nums + [1]

        # Starting from burst one balloon.
        for length in range(1, n + 1):
            # The beginning of burst length balloon.
            for i in range(1, n - length + 2):
                # The end of burst length balloon.
                j = i + length - 1
                for k in range(i, j + 1):
                    c[i][j] = max(c[i][j], c[i][k - 1] + nums[i - 1] * nums[k] * nums[j + 1] + c[k + 1][j])

        return c[1][n]
