# coding: utf-8
"""
The numbers 7 and 23 are relatively prime and therefore there must exist integers a and b such that 7a+23b=1. Find such a pair of integers (a,b) with the smallest possible a>0. Given this pair, can you determine the inverse of 7 in Z23? 

Enter below comma separated values for a, b, and for 7−1 in Z23.

Solution:
Use extended euclid to find a and b and inverse of 7
"""

def egcd(x, y):
    a,b, u,v = 0,1, 1,0
    while x != 0:
        q, r = y//x, y%x
        m, n = a-u*q, b-v*q
        y,x, a,b, u,v = x,r, u,v, m,n
    return y, a, b

x = 7
y = 23

y, a, b = egcd(x, y)

print "a =", a
print "b =", b

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

find_inv = 7
m = 23

print "Modular inverse for", find_inv, "=", modinv(find_inv, m)


