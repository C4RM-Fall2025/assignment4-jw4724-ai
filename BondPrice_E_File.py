def getBondDuration(y, face, couponRate, m, ppy=1):
    if ppy <= 0:
        ppy = 1
    r = y / ppy
    n = int(m * ppy)
    c = face * couponRate / ppy

    price = 0.0
    for t in range(1, n):
        price += c / ((1 + r) ** t)
    price += (c + face) / ((1 + r) ** n)

    numer = 0.0
    for t in range(1, n):
        numer += t * (c / ((1 + r) ** t))
    numer += n * ((c + face) / ((1 + r) ** n))

    return (numer / price) / ppy


