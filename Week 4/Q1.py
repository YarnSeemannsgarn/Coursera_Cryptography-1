"""
An attacker intercepts the following ciphertext (hex encoded): 

   20814804c1767293b99f1d9cab3bc3e7 ac1e37bfb15599e5f40eef805488281d 

He knows that the plaintext is the ASCII encoding of the message "Pay Bob 100$" (excluding the quotes). He also knows that the cipher used is CBC encryption with a random IV using AES as the underlying block cipher. Show that the attacker can change the ciphertext so that it will decrypt to "Pay Bob 500$". What is the resulting ciphertext (hex encoded)? This shows that CBC provides no integrity.

Solution:
Just create IV' as mentioned in the lecture:
IV' = IV xor (...100$...) xor (...500$...)
"""

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

pt = "Pay Bob 100$"
ct = "20814804c1767293b99f1d9cab3bc3e7ac1e37bfb15599e5f40eef805488281d".decode("hex")
iv = ct[:16]

ind = pt.index("1")
iv_new = iv[:ind] + strxor(strxor(iv[ind], "1"), "5") + iv[ind+1:]
ct_new = iv_new + ct[16:]

print "new ct: %s" % ct_new.encode("hex")
