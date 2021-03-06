# -*- coding: utf-8 -*-
"""
Your goal in this project is to break RSA when the public modulus N is generated incorrectly. This should serve as yet another reminder not to implement crypto primitives yourself. 

Normally, the primes that comprise an RSA modulus are generated independently of one another. But suppose a developer decides to generate the first prime p by choosing a random number R and scanning for a prime close by. The second prime q is generated by scanning for some other random prime also close to R. We show that the resulting RSA modulus N=pq can be easily factored. 

Suppose you are given a composite N and are told that N is a product of two relatively close primes p and q, namely p and q satisfy 
   |p−q|<2N1/4    (*) 
Your goal is to factor N. 

Let A be the arithmetic average of the two primes, that is A=p+q2. Since p and q are odd, we know that p+q is even and therefore A is an integer. 

To factor N you first observe that under condition (*) the quantity N−−√ is very close to A. In particular 
   A−N−−√<1 
as shown below. But since A is an integer, rounding N−−√ up to the closest integer reveals the value of A. In code, A=ceil(sqrt(N)) where "ceil" is the ceiling function. Visually, the numbers p,q,N−−√ and A are ordered as follows:


Since A is the exact mid-point between p and q there is an integer x such that p=A−x and q=A+x. But then 
   N=pq=(A−x)(A+x)=A2−x2 and therefore x=A2−N−−−−−−√ 
Now, given x and A you can find the factors p and q of N since p=A−x and q=A+x. 

In the following challenges, you will factor the given moduli using the method outlined above. To solve this assignment it is best to use an environment that supports multi-precision arithmetic and square roots. In Python you could use the gmpy2 module. In C you can use GMP. 

Factoring challenge #1: The following modulus N is a products of two primes p and q where |p−q|<2N1/4. Find the smaller of the two factors and enter it as a decimal integer.
N = 17976931348623159077293051907890247336179769789423065727343008115 \
    77326758055056206869853794492129829595855013875371640157101398586 \
    47833778606925583497541085196591615128057575940752635007475935288 \
    71082364994994077189561705436114947486504671101510156394068052754 \
    0071584560878577663743040086340742855278549092581


Factoring challenge #2: The following modulus N is a products of two primes p and q where |p−q|<211N1/4. Find the smaller of the two factors and enter it as a decimal integer.
Hint: in this case A−N−−√<220 so try scanning for A from N−−√ upwards, until you succeed in factoring N.
N = 6484558428080716696628242653467722787263437207069762630604390703787 \
    9730861808111646271401527606141756919558732184025452065542490671989 \
    2428844841839353281972988531310511738648965962582821502504990264452 \
    1008852816733037111422964210278402893076574586452336833570778346897 \
    15838646088239640236866252211790085787877


Factoring challenge #3: (extra credit) The following modulus N is a products of two primes p and q where |3p−2q|<N1/4. Find the smaller of the two factors and enter it as a decimal integer. 
Hint: use the calculation below to show that 6N−−−√ is close to 3p+2q2 and then adapt the method above to factor N.
N = 72006226374735042527956443552558373833808445147399984182665305798191 \
    63556901883377904234086641876639384851752649940178970835240791356868 \
    77441155132015188279331812309091996246361896836573643119174094961348 \
    52463970788523879939683923036467667022162701835329944324119217381272 \
    9276147530748597302192751375739387929


The only remaining mystery is why A−N−−√<1. This follows from the following simple calculation. First observe that 
   A2−N=(p+q2)2−N=p2+2N+q24−N=p2−2N+q24=(p−q)2/4 
Now, since for all x,y:  (x−y)(x+y)=x2−y2 we obtain 
   A−N−−√=(A−N−−√)A+N√A+N√=A2−NA+N√=(p−q)2/4A+N√ 
and since N−−√≤A it follows that 
   A−N−−√≤(p−q)2/42N√=(p−q)28N√ 
By assumption (*) we know that (p−q)2<4N−−√ and therefore 
   A−N−−√≤4N√8N√=1/2 
as required. 

Further reading: the method described above is a greatly simplified version of a much more general result on factoring when the high order bits of the prime factor are known. 

Enter the answer for factoring challenge #1 in the box below: 
"""

from gmpy2 import mpz, isqrt, invert, digits, powmod

def q1():
    n = mpz('17976931348623159077293051907890247336179769789423065727343008115' + 
            '77326758055056206869853794492129829595855013875371640157101398586' +
            '47833778606925583497541085196591615128057575940752635007475935288' +
            '71082364994994077189561705436114947486504671101510156394068052754' +
            '0071584560878577663743040086340742855278549092581')

    a = isqrt(n) + 1

    return a - isqrt(a**2 - n)


def q2():
    n = mpz('6484558428080716696628242653467722787263437207069762630604390703787' +
            '9730861808111646271401527606141756919558732184025452065542490671989' +
            '2428844841839353281972988531310511738648965962582821502504990264452' +
            '1008852816733037111422964210278402893076574586452336833570778346897' +
            '15838646088239640236866252211790085787877')

    a = isqrt(n)

    while True:
        try:
            x = isqrt(a**2 - n)
            if n == (a - x) * (a + x):
                break

        except ValueError:
            pass
        

        a += 1

    return a - x


def q3():
    n = mpz('72006226374735042527956443552558373833808445147399984182665305798191' + 
            '63556901883377904234086641876639384851752649940178970835240791356868' +
            '77441155132015188279331812309091996246361896836573643119174094961348' +
            '52463970788523879939683923036467667022162701835329944324119217381272' +
            '9276147530748597302192751375739387929')
    
    a_ = isqrt(n * 24) + 1
    
    d = (a_**2) - 24*n

    assert d > 0

    p = (a_ - isqrt(d)) / 6

    return min(p, n/p)


def q4():
    c = mpz('22096451867410381776306561134883418017410069787892831071731839143676135600120538004282329650473509424343946219751512256' +
            '46583996794288946076454204058156474898801373486412045232522932017648791666640299750918872997169052608322206777160001932' + 
            '9260870009579993724077458967773697817571267229951148662959627934791540')

    n = mpz('17976931348623159077293051907890247336179769789423065727343008115' + 
            '77326758055056206869853794492129829595855013875371640157101398586' +
            '47833778606925583497541085196591615128057575940752635007475935288' +
            '71082364994994077189561705436114947486504671101510156394068052754' +
            '0071584560878577663743040086340742855278549092581')

    e = mpz(65537)

    a = isqrt(n) + 1
    x = isqrt(a**2 - n)

    p = a - x
    q = a + x

    fi = (p-1) * (q-1)

    d = invert(e, fi)

    r = powmod(c, d, n)
    
    m = digits(r, 16).split('00')[1]
    
    return m.decode('hex')

print q1()
print q2()
print q3()
print q4()
