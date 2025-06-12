print("tabel kebenaran implikasi, konvers, invers")

def implikasi(P, Q):
    return not P or Q

def konvers(P, Q):
    return implikasi(Q, P)

def invers(P, Q):
    return implikasi(not P, not Q)

def kontraposisi(P, Q):
    return implikasi(not Q, not P)

def tabel_kebenaran():
    print("\n")
    print("tabel kebenaran proposisi bersyarat")
    print("-" * 47)
    print("P\tQ\tP->Q\tQ->P\t-P->-Q\t-Q->-P")
    for P in [True, False]:
         for Q in [True, False]:
            print(f"{P}\t{Q}\t{implikasi(P, Q)}\t{konvers(P, Q)}\t{invers(P, Q)}\t{kontraposisi(P, Q)}")

tabel_kebenaran()
