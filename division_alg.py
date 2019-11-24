def division_alg(F,f):
    """Divide f by F[0],...,F[s-1].

    F a list of polynomials.
    All polynomials in a ring with monomial ordering."""
    a = [0]*len(F)
    r = 0
    p = f
    while p != 0:
        i = 0
        divisionoccured = False
        while i < len(F) and divisionoccured == False:
            if p%F[i].lt() == 0:
                a[i] = a[i] + p.lt()//F[i].lt()
                p = p - F[i]*p.lt()//F[i].lt()
                divisionoccured = True
            else:
                i = i + 1
        if divisionoccured == False:
            r = r + p.lt()
            p = p - p.lt()
    return a,r
