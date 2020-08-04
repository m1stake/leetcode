from typing import List


class Solution:

    """
    s 可能为空，且只包含从 a-z 的小写字母
    p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *
    """

    def isMatch(self, s: str, p: str) -> bool:

        # 将p分块，.; .*; ?*; ?...
        pattern = self.compile(p)
        print(pattern)

        return self.matchs(s, pattern)

    def matchs(self, s: str, pattern: List[str]):
        # 逐块匹配
        for ptn in pattern:
            if ptn == '.':
                if len(s) >= 1:
                    return self.matchs(s[1:], pattern[1:])
                else:
                    return False
            elif ptn == '.*':
                pattern = pattern[1:]
                for i in range(len(s) + 1):
                    if self.matchs(s[i:], pattern):
                        return True
                return False
            elif ptn.endswith('*'):
                pattern = pattern[1:]
                c = ptn[0]

                if self.matchs(s, pattern):
                    return True

                for i in range(0, len(s)):
                    if s[i] == c:
                        if self.matchs(s[i + 1:], pattern):
                            return True
                    else:
                        return False
            else:
                if len(s) >= len(ptn):
                    if ptn == s[:len(ptn)]:
                        return self.matchs(s[len(ptn):], pattern[1:])
                    else:
                        return False
                else:
                    return False

        if len(s) > 0:
            return False
        else:
            return True

    def compile(self, p):

        ptn = []

        pre = None
        i = 0
        while i < len(p):
            cc = p[i]
            next_c = p[i + 1] if (i < len(p) - 1) else None

            if cc == '.':
                if next_c == '*':
                    ptn.append('.*')
                    i += 1
                    pre = '*'
                else:
                    ptn.append('.')
                    pre = '.'
            else:
                if next_c == '*':
                    ptn.append(cc + '*')
                    i += 1
                    pre = '*'
                else:
                    if pre in ['.', '*']:
                        ptn.append(cc)
                    elif ptn:
                        ptn[-1] += cc
                    else:
                        ptn.append(cc)
                    pre = cc
            i += 1
        return ptn


#print(
#    Solution().compile(''),
#    Solution().compile('.*..abc*a'),
#)

print(
    Solution().isMatch('aa', 'a'),
    Solution().isMatch('aa', 'a*'),
    Solution().isMatch('aab', '.*'),
    Solution().isMatch('aab', 'c*a*b'),
    Solution().isMatch('mississippi', 'mis*is*p*.'),
    Solution().isMatch('ab', '.*c'),

)
