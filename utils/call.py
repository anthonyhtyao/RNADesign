from subprocess import Popen, PIPE, STDOUT
import re

def get_float(r):
    """
    Return all float in a given text
    """
    f = re.compile('[-]*\d+\.\d+')
    res = f.findall(r)
    return list(map(float,res))

def get_energy(seq,stc):
    """
    For a given pair of RNA sequence and secondary structure in dot-bracket notation, 
    returns mfe and fee
    """
    p = Popen(["RNAfold","-C","--enforceConstraint","-p0"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    out, err = p.communicate((seq+'\n'+stc).encode())
    floats = get_float(out.decode())
    return floats[0], floats[1]

def get_subopt(seq,stc,delta):
    """
    For a given RNA sequence, secondary structure pattern in dot-bracket notation, and delta, 
    returns all possible foldings matching the given pattern whose energy is between mfe and 
    mfe+delta
    """
    p = Popen(["RNAsubopt","-C","--enforceConstraint","--deltaEnergy={}".format(delta)],
            stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    out, err = p.communicate((seq+'\n'+stc).encode())
    res = out.decode().split('\n')
    mfe = get_float(res[0])[0]
    return res[1:]
