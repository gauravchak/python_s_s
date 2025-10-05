def transform(input_str: str) -> str:

    l = input_str
    yay_part = l.split()
    N = int(yay_part[0])
    P = int(yay_part[1])
    D = int(yay_part[2])

    n = str(N)
    p = len(n) - P

    def findp(n, p):
        nst = []
        for i in n:
            nst.append(i)
        return nst[p]

    x = findp(n, p)

    def findu(num):
        l = len(str(num))
        emt = []
        for i in str(num):
            emt.append(i)
        return emt[l - 1]

    def findl(num):
        emt = []
        for i in str(num):
            emt.append(i)
        return emt[0]

    def main(x, D):
        x = int(x)
        if x < 5:
            x = x + D
            x = findu(x)
            return x
        elif x > 4:
            x = x - D
            x = abs(x)
            x = findl(x)
            return x

    x = main(x, D)

    def replace(n, p, x):
        nst = []
        for i in n:
            nst.append(i)
        nst[p] = x
        for i in (p + 1, len(n) - 1):
            nst[i] = str(0)
        y = "".join(nst)
        return y

    return replace(n, p, x)


def transform_2(input_str: str) -> str:

    N, P, D = input_str.split()
    P, D = int(P), int(D)
    s = list(str(N))  # Needed because string s wouldn't support injection
    idx = len(s) - P  # index of P-th digit from right
    digit = int(s[idx])  # P-th from last digit

    if 0 <= digit <= 4:
        new_digit = (digit + D) % 10
    else:
        diff = abs(digit - D)
        new_digit = int(str(diff)[0])  # leftmost digit

    s[idx] = str(new_digit)

    # Replace digits to right of P-th digit with 0
    for i in range(idx + 1, len(s)):
        s[i] = "0"

    return "".join(s)
