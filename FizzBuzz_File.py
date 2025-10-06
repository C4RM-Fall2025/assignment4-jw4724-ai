def FizzBuzz(start, finish):
    out = []
    for n in range(start, finish + 1):
        if n % 15 == 0:
            out.append("fizzbuzz")
        elif n % 3 == 0:
            out.append("fizz")
        elif n % 5 == 0:
            out.append("buzz")
        else:
            out.append(n)
    return out

