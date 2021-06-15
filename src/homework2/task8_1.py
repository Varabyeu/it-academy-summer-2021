#Some numbers have funny properties. For example:
#89 --> 8¹ + 9² = 89 * 1
#695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
#46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
#Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p
#we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.
#In other words:
#Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
#If it is the case we will return k, if not return -1.
#Note: n and p will always be given as strictly positive integers.


def dig_pow(n, p):
    n_len = len(str(n))
    x = 1
    num = 0
    all_num = 0
    z = 0
    while x <= n_len:
        z += num * 10**(n_len - x + 1)
        num = (n - z) // (10**(n_len - x))
        num_p = num ** (p + x - 1)
        all_num += num_p
        x += 1
    k = (all_num / n)
    if k * 10 % 10:
        return -1
    else:
        return k

print(dig_pow(46288, 3))
