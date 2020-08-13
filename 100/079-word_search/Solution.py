from typing import List


class Solution:

    """
    太慢，内存占用太多
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        position_map = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                if c in position_map:
                    position_map[c].append((i, j))
                else:
                    position_map[c] = [(i, j)]

        placeholder = set()

        return self.exist0(position_map, None, word, placeholder)

    def exist0(self, position_map, pre_position, word, placeholder):

        if not word:
            return True

        a = word[0]
        if a in position_map:
            aps = position_map[a]
            for ap in aps:
                if ap not in placeholder and (pre_position is None or self.around(ap, pre_position)):
                    placeholder.add(ap)
                    if not self.exist0(position_map, ap, word[1:], placeholder):
                        placeholder.remove(ap)
                    else:
                        return True
                else:
                    pass
            return False
        else:
            return False

    def around(self, ap, pre_position):
        # 上下左右
        apc = ap[0] + ap[1]
        ppc = pre_position[0] + pre_position[1]

        if ap[0] == pre_position[0] - 1 and ap[1] == pre_position[1] \
                or ap[0] == pre_position[0] + 1 and ap[1] == pre_position[1] \
                or ap[0] == pre_position[0] and ap[1] + 1 == pre_position[1] \
                or ap[0] == pre_position[0] and ap[1] - 1 == pre_position[1]:
            return True
        else:
            return False


print(
    # Solution().exist(
    #     [
    #         ['T', 'H', 'A'],
    #         ['S', 'K', 'N']
    #     ],
    #     'THANKS'
    # ),
    # Solution().exist(
    #     [
    #         ['T', 'H', 'A'],
    #         ['S', 'K', 'N']
    #     ],
    #     'THAANKS'
    # ),
    # Solution().exist(
    #     [
    #         ['A','B','C','E'],
    #         ['S','F','C','S'],
    #         ['A','D','E','E']
    #     ],
    #     'ABCCED'
    # ),
    Solution().exist(
        [["F","Y","C","E","N","R","D"],
         ["K","L","N","F","I","N","U"],
         ["A","A","A","R","A","H","R"],
         ["N","D","K","L","P","N","E"],
         ["A","L","A","N","S","A","P"],
         ["O","O","G","O","T","P","N"],
         ["H","P","O","L","A","N","O"]],
        "USA"
    )
)




