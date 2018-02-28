from ..utils.structure import bracket_to_index

class Tree:

    def __init__(self):

    @classmethod
    def from_bracket(cls, inst):
        """
        Convert bracket-dot presentation to tree presentation
        """
        index = bracket_to_index(inst)
