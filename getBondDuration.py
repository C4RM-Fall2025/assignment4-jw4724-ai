def getBondDuration(y, face, couponRate, m, ppy=1):
    """
    Macaulay duration in YEARS.

    y: annual yield to maturity (decimal, e.g., 0.03)
    face: face value (e.g., 2_000_000)
    couponRate: annual coupon rate (decimal, e.g., 0.04)
    m: years to maturity (e.g., 10)
    ppy: payments per year (1=annual, 2=semiannual, ...)
    """
    if ppy <= 0:
        ppy = 1

    r = y / ppy                 # per-period yield
    n = int(m * ppy)            # number of periods
    c = face * couponRate / ppy # coupon per period

    # Price (PV of coupons + redemption)
    price = 0.0
    for t in range(1, n):
        price += c / ((1 + r) ** t)
    price += (c + face) / ((1 + r) ** n)

    # Macaulay duration numerator: sum( t * PV(CF_t) )
    numer = 0.0
    for t in range(1, n):
        numer += t * (c / ((1 + r) ** t))
    numer += n * ((c + face) / ((1 + r) ** n))

    # Convert period-duration to years
    duration_years = (numer / price) / ppy
    return duration_years
