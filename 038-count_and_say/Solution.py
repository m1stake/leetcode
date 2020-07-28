

class Solution:

    def countAndSay(self, n: int) -> str:
        """
        1
        11
        21
        1211
        """

        if n == 1:
            return "1"

        pre_say = "1"

        for _ in range(n - 1):
            pre_say = self.say(pre_say)

        return pre_say

    def say(self, pre_say):

        s = ''
        cc = None
        count = 0

        for c in pre_say:
            if c == cc:
                count += 1
            else:
                if count > 0:
                    s += str(count) + cc
                cc = c
                count = 1

        if count > 0:
            s += str(count) + cc
        return s


print(
    Solution().countAndSay(1),
    Solution().countAndSay(2),
    Solution().countAndSay(3),
    Solution().countAndSay(4),
    Solution().countAndSay(5),
    Solution().countAndSay(6),
    Solution().countAndSay(30),

)



