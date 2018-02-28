def is_parenthesized(inst):
    """
    Returns True if the given bracket-dot presented secondary structure is well parenthesized
    Otherwuse, returns False
    """
    n = 0
    for c in inst:
        if c == '(':
            n += 1
        elif c == ')':
            n -= 1
    return n == 0

def bracket_to_index(inst):
    """
    For a given bracket-dot presented secondary structure S, the function returns an iterger list L.
    L[i] equals to j if S[i] and S[j] are a pair of parentheses.
    """
    res = [ -1 for c in inst]
    tmp = []
    for i,c in enumerate(inst):
        if c == '(':
            tmp.append(i)
        elif c == ')':
            j = tmp.pop()
            res[i], res[j] = j, i
    return res

def decomposition(inst):
    def aux(ind,lst):
        tmp = []
        res = []
        k = ind
        while True:
            if k >= len(lst):
                break
            if lst[k] == -1 :
                k += 1
            elif lst[k] > k:
                tmp.append((k, lst[k]))
                res += aux(k+1,lst)
                k = lst[k] + 1
            else:
                break
        return res + [ tmp+[(ind-1,k)]]

    index = bracket_to_index(inst)
    res = aux(0,index)
    return sorted(list(map(sorted,res)))


if __name__ == '__main__':
    s = '((...))'
    print(decomposition(s))
