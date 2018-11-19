## Classic List

  - 480 Sliding Window Median
    - bisect is your friend
      - import bisect
      - bisect.insort(a, val)
      - bisect.remove(val)
      - bisect.bisect_left(a, val)

  - 239 Sliding Window Maximum
    - Deque is your friend
    - Keep a non-increase deque of maximum

  - 146 LRU Cache
    - Insert and remove O(1) -> Double Linked List

  - 10 Regular Expression Matching
    - Carefull about the logic
    - 2-D DP

  - 239 Sliding Window Maximum
    - Use deque
    - Keep decreasing max

  - 312 Burst Balloons
    - Dynamic programming
    - O(N^3)

  - 336 Palindrome Pairs
    - Use dictionary
    - Very tricky
      - Check all prefixes, if any prefix is palindrome and its remaining string reversed is in the word list, then score.
      - Check all suffixes, if any suffix is palindrome and its remaining string reversed is in the word list, then score.

  - 140 Word Break II
    - DP, bottom up
      - Memory limit exceeded
    - Recursion + Dictionary == Dynamic Programming, top down, only call recursively when inDict is true
      - wordBreak('catsanddo') + inDict('g')
      - U wordBreak('catsandd') + inDict('og')
      - U ...
      - U wordBreak('') + inDict('catsanddog')
