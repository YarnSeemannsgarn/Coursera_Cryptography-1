m1 = "attack at dawn".encode("hex")
m2 = "attack at dusk".encode("hex")
c1 = "0x6c73d5240a948c86981bc294814d"
otp = "%x" % (int(m1, 16) ^ int(c1, 16))

print "m1:  " + m1
print "m2:  " + m2
print "c1:  " + c1
print "otp: " + otp

c2 = "%x" % (int(m2, 16) ^ int(otp, 16))

print "c2:  " + c2
