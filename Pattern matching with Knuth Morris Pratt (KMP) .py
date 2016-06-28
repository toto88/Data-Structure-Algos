# Knuth Morris Pratt algorithm
# o(n+m) ~ o(m)


def compute_kmp_fail (P):
    m = len(P)
    fail = [0]*m
    j=1
    k=0

    while j<m:
        if P[j]==P[k]:
            fail[j]=k+1
            j=j+1
            k=k+1

        elif k>0:
            k=fail[k-1]
        else:
            j=j+1

    return fail

def find_kmp(T,P):
    n,m = len(T),len(P)

    if m==0: return 0

    fail=compute_kmp_fail(P)

    j=0
    k=0

    while j<n:
        if T[j] == P[k]:
            if k==m-1:
                return j-m+1
            j=j+1
            k=k+1
        elif k>0:
            k=fail[k-1]
        else:
            j=j+1


    return -1


T=["T","C","A","C","A","G","C","A","T","A","C","A","G","T","C","A"]
P=["G","C","A"]

i=find_kmp(T,P)
print i