from utils.structure import decomposition
from models.base import LoopNode


class Tree:

    def __init__(self):
        self.root = None

    @classmethod
    def from_bracket(cls, inst):
        """
        Convert bracket-dot presentation to tree presentation
        """
        tree = cls()
        base_lst = decomposition(inst)
        parent_dict = {}
        for ind, e in enumerate(base_lst):
            if ind == 0:
                node = LoopNode(e)
                tree.root = node
            else:
                node = LoopNode(e, parent = parent_dict[e[0]])
            if len(e) > 1:
                for bp in e[1:]:
                    parent_dict[bp] = node
        return tree
