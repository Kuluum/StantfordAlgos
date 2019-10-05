def recursiveMultiply(x, y):
    n = max(len(str(x)), len(str(y)))

    if n <= 2:
        return x*y

    tn = 10 ** (n//2)

    a = x // tn
    b = x % tn
    c = y // tn
    d = y % tn

    ac = recursiveMultiply(a, c)
    bd = recursiveMultiply(b, d)
    ab_cd = recursiveMultiply(a+b, c+d)
    ad_bc = ab_cd - ac - bd

    return tn**2 * ac + tn * ad_bc + bd


print(recursiveMultiply(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))
print(3141592653589793238462643383279502884197169399375105820974944592*2718281828459045235360287471352662497757247093699959574966967627)
