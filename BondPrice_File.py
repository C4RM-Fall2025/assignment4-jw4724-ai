def getBondPrice(y, face, couponRate, m, ppy=1):
    if ppy <= 0:
        ppy = 1
    r = y / ppy
    n = int(m * ppy)
    c = face * couponRate / ppy
    price = 0.0
    for t in range(1, n + 1):
        price += c / ((1 + r) ** t)
    price += face / ((1 + r) ** n)
    return price
