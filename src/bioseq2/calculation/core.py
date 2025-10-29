# SeqCal module
def countBase(seq, base): 
    return seq.count(base.upper())

def gcContent(seq): 
    return (countBase(seq, 'G') + countBase(seq, 'C'))/len(seq)

def atContent(seq):
    return (countBase(seq, 'A') + countBase(seq, 'T'))/len(seq)

def countBasesDict(seq):
    basesM = {}
    for base in seq:
        basesM[base] = basesM.get(base, 0)+1
    return basesM

if __name__ == "__main__":
    # Test
    seq = "ATGGGccGTAGAATTCTTGCaaGCCCGT"
    print("Sequence:", seq)
    print("A count:", countBase(seq, 'A'))
    print("T count:", countBase(seq, 'T'))
    print("G count:", countBase(seq, 'G'))
    print("C count:", countBase(seq, 'C'))
    print("GC content:", gcContent(seq))
    print("AT content:", atContent(seq))
    print("Base counts:", countBasesDict(seq))