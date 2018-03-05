from collections import namedtuple
from utils.structure import decomposition

BasePair = namedtuple('BasePair', ('fst','snd'))

class Loop:
    """
    A class for basic components of RNA secondary structure, including Stacking Pair, Hairpin Loop,
    Internal Loop and Multiple Loop
    """

    def __init__(self, lst):
        bp_list = list(map(lambda t: BasePair(*t), lst))
        nb_bp = len(bp_list)
        self.closing_bp = bp_list[0]
        self.enclosing_bp = bp_list[1:]

        # Hairpin Loop
        if nb_bp == 1:
            self.name = 'Hairpin Loop'
            self.label = 'H'
        
        # Stacking Pair and Internal Loop
        elif nb_bp == 2:
            bp_1 = self.closing_bp
            bp_2 = self.enclosing_bp[0]
            if (abs(bp_1.fst-bp_2.fst) == 1) and (abs(bp_1.snd-bp_2.snd) == 1):
                self.name = 'Stacking Pair'
                self.label = 'S'
            else:
                self.name = 'Internal Loop'
                self.label = 'I'
            
        # Multiple Loop
        elif nb_bp > 2:
            self.name = 'Multiple Loop'
            self.label = 'M'

class LoopNode(Loop):

    def __init__(self, lst, parent=None):
        super().__init__(lst)
        self.parent = parent
        self.children = []

    def __str__(self):
        return self.name

