def toh(n,source,destination,auxilary):
    if n>=1:
        toh(n-1,source,auxilary,destination)
        movedisk(source,destination)
        toh(n-1,auxilary,source,destination)

def movedisk(source,destination):
    print source,"->",destination

toh(10,"A","B","C")