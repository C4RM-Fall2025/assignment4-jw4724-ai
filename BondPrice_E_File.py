def getBondPrice_E(face, couponRate, yc):
    price = 0.0
    n = len(yc)
    coupon = face * couponRate

    for i in range(n):
        rate = yc[i]
        cashflow = coupon
        if i == n - 1:
            cashflow += face
        price += cashflow / ((1 + rate) ** (i + 1))

    return price


