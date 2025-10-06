def getBondPrice_Z(face, couponRate, times, yc):
    coupon = face * couponRate
    price = 0.0
    n = len(times)

    for idx in range(n):
        rate = yc[idx]
        t = times[idx]
        cashflow = coupon + face if idx == n - 1 else coupon
        price += cashflow / ((1 + rate) ** t)

    return price


