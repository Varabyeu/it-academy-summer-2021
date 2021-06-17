# Take 2 strings s1 and s2 including only letters from ato z.
# Return a new sorted string, the longest possible,
# containing distinct letters - each taken only once -
# coming from s1 or s2.
# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"
# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"


def longest(a1, a2):
    a1 = a1 + a2
    str_new = ''
    for lit in a1:
        if lit not in str_new and lit != ' ':
            str_new += lit
    return str_new


print(longest("aretheyhere", "yestheyarehere"))
