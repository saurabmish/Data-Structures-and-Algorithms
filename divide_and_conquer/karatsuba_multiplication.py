'''Grade School Multiplication on Steroids

Time Complexity: O(n^(log 3))
'''

def karatsuba(x,y):

    table = {
        (0, 1): 0,  (1, 0): 0,   (1, 1): 1,
        (0, -1): 0, (-1, 0): 0,  (-1, -1): 1,
        (0, 0):0,   (-1, 1): -1, (1, -1): -1,
    }

    n = max(x.bit_length(), y.bit_length())

    if n < 2:
        return table[(x, y)]
    else:
        n = (n + 1) >> 1
        b = x >> n
        a = x - (b << n)
        d = y >> n
        c = y - (d << n)

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        abcd = karatsuba((a + b), (c + d)) - ac - bd
        return ac + ((abcd) << n) + (bd << (n << 1))
