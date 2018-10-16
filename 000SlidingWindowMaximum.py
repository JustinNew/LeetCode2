# 239. Sliding Window Maximum

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        import heapq

        if len(nums) == 0:
            return []

        window = [-1 * i for i in nums[:k]]
        res = []

        heapq.heapify(window)
        for i in range(k, len(nums)):
            res.append(-1 * window[0])
            window.remove(-1 * nums[i - k])
            heapq.heapify(window)
            heapq.heappush(window, -1 * nums[i])

        res.append(-1 * window[0])

        return res

    '''
    Try to get it in linear time.
    Use stack to keep the non-increase list of maximum number.
    '''

    def maxSlidingWindow(self, nums, k):

        from collections import deque
        
        if len(nums) == 0:
            return []
        
        m = deque()
        res = []

        for i in range(k):
            if len(m) == 0:
                m.append(nums[i])
            elif nums[i] <= m[-1]:
                m.append(nums[i])
            else:
                while len(m) != 0 and m[-1] < nums[i]:
                    m.pop()
                m.append(nums[i])

        res.append(m[0])
            
        for i in range(k, len(nums)):

            # Need to pop out nums[i - k]
            # If m[0] equal it, pop out first.
            if m[0] == nums[i - k]:
                m.popleft()

            # Update maximum list 
            if len(m) == 0:
                m.append(nums[i])
            elif nums[i] <= m[-1]:
                m.append(nums[i])
            else:
                while len(m) != 0 and m[-1] < nums[i]:
                    m.pop()
                m.append(nums[i])

            # Add current maximum.
            res.append(m[0])

        return res
