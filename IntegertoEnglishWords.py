# 273. Integer to English Words

# Facebook Tag

'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
'''

class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return 'Zero'
        
        d = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten',
             11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 
             18:'Eighteen', 19:'Nineteen', 20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy',         
             80:'Eighty', 90:'Ninety'}

        def belowThousand(val):

            res = ''
            if val >= 100:
                t = int(val / 100)
                val = val % 100
                res += d[t] + ' Hundred'

            if val >= 20:
                t = int(val / 10)
                t *= 10
                val = val % 10
                if res != '':
                    res += ' ' + d[t]
                else:
                    res += d[t]

            if val > 0:
                if res != '':
                    res += ' ' + d[val]
                else:
                    res += d[val]

            return res

        ans = ''
        units = {10 ** 12:'Trillion', 10 ** 9:'Billion', 10 ** 6:'Million', 10 ** 3:'Thousand'}
        keys = [i for i in units.keys()]
        keys.sort(reverse=True)
        for u in keys:
            if num >= u:
                t_u = int(num / u)
                num = num % u
                if ans != '':
                    ans += ' ' + belowThousand(t_u) + ' ' + units[u]
                else:
                    ans += belowThousand(t_u) + ' ' + units[u]

        if num != 0:
            if ans != '':
                ans += ' ' + belowThousand(num)
            else:
                ans += belowThousand(num)
        
        return ans
