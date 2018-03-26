import itertools

class DesignIter:
    def __init__(self, *iterables):
        self.source = itertools.product(*iterables)
        self.cache = []
        self.cache_len = 0
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count >= self.cache_len:
             while True:
                try:
                    seq = next(self.source)
                    if __filter(seq):
                        checked = True
                        self.cache.append(seq)
                        self.cache_len += 1
                        return seq

                except StopIteration:
                    raise StopIteration
            
        else:
            return self.cache[self.count]

def __filter(seq):
    return True
