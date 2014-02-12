"""
In this project you will experiment with a padding oracle attack against a toy web site hosted at crypto-class.appspot.com. Padding oracle vulnerabilities affect a wide variety of products, including secure tokens. This project will show how they can be exploited. We discussed CBC padding oracle attacks in Lecture 7.6, but if you want to read more about them, please see Vaudenay's paper. 

Now to business. Suppose an attacker wishes to steal secret information from our target web site crypto-class.appspot.com. The attacker suspects that the web site embeds encrypted customer data in URL parameters such as this:
http://crypto-class.appspot.com/po?er=f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4
That is, when customer Alice interacts with the site, the site embeds a URL like this in web pages it sends to Alice. The attacker intercepts the URL listed above and guesses that the ciphertext following the "po?er=" is a hex encoded AES CBC encryption with a random IV of some secret data about Alice's session. 

After some experimentation the attacker discovers that the web site is vulnerable to a CBC padding oracle attack. In particular, when a decrypted CBC ciphertext ends in an invalid pad the web server returns a 403 error code (forbidden request). When the CBC padding is valid, but the message is malformed, the web server returns a 404 error code (URL not found). 

Armed with this information your goal is to decrypt the ciphertext listed above. To do so you can send arbitrary HTTP requests to the web site of the form
http://crypto-class.appspot.com/po?er="your ciphertext here"
and observe the resulting error code. The padding oracle will let you decrypt the given ciphertext one byte at a time. To decrypt a single byte you will need to send up to 256 HTTP requests to the site. Keep in mind that the first ciphertext block is the random IV. The decrypted message is ASCII encoded. 

To get you started here is a short Python script that sends a ciphertext supplied on the command line to the site and prints the resulting error code. You can extend this script (or write one from scratch) to implement the padding oracle attack. Once you decrypt the given ciphertext, please enter the decrypted message in the box below. 

This project shows that when using encryption you must prevent padding oracle attacks by either using encrypt-then-MAC as in EAX or GCM, or if you must use MAC-then-encrypt then ensure that the site treats padding errors the same way it treats MAC errors.

Solution:
Look for good paddings
"""

import urllib2
import sys

def strxor(s1, s2):
    return "".join([ chr(ord(c2) ^ ord(c1)) for (c1, c2) in zip(s1, s2)])

def strrep(s, sub, pos):
    endpos = pos + len(sub)
    return s[:pos] + sub + s[endpos:]

TARGET = 'http://crypto-class.appspot.com/po?er='
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:
            return e.code
        return 200

start_query='f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'.decode('hex')

def try_byte(query, byte_at, pad):
    po = PaddingOracle()
    g200 = None

    def try_guess(g):
        g200 = 0
        last = query[byte_at]
        last = chr(ord(last) ^ pad ^ g)
        q = strrep(query, last, byte_at)
        http_status = po.query(q.encode('hex'))
        if http_status == 404:
            print "Good padding found: 0x%02x" % g
            return g
        if http_status == 200:
            g200 = g
        # if http_status not in (200, 403):
        print "  0x%02x failed (%d)..." % (g, http_status)
        return g200

    if try_guess(0x09): return 0x09
    if try_guess(0x20): return 0x20

    for i in xrange(0x7f, 0x00, -1):
        if try_guess(i): return i

    for i in xrange(0x80, 0xFF):
        if try_guess(i): return i

    if g200: print "Assuming: 0x%02x" % g200
    else: print 'Failed to guess query[%d]' % byte_at
    return g200

def oracle_byte_s(query, guess, start, end):
    for i in xrange(end - 1 - len(guess), start - 1, -1):
        print 'Guessing query[%d]' % i
        padlen = end - i
        subst = strxor(strxor(query[i+1:end], guess), chr(padlen) * padlen)
        q = strrep(query, subst, i+1)
        g = try_byte(q, i, padlen)
        if g is None:
            print '  Failed.'
            return None
        guess = chr(g) + guess
    return guess

def oracle_bytes(query, start, end):
    return oracle_byte_s(query, '', start, end)

if __name__ == "__main__":
    s3 = oracle_bytes(start_query, 32, 48)
    s2 = oracle_bytes(start_query[:48], 16, 32)
    s1 = oracle_bytes(start_query[:32], 0, 16)
    print s1 + s2 + s3
