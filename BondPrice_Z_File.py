def getBondPrice_Z(face, couponRate, times, yc):
    price = 0.0
    coupon = face * couponRate
    T = len(times)
    for i, (t, y) in enumerate(zip(times, yc), start=1):
        cash = coupon if i < T else coupon + face
        price += cash / ((1 + y) ** t)
    return price

