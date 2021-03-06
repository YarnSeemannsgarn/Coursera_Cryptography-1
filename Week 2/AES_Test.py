from Crypto.Cipher import AES
from Crypto.Util import Counter

CBC_KEY = "140b41b22a29beb4061bda66b6747e14".decode("hex")
CBC_CIPHER1 = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81".decode("hex")
CBC_CIPHER2 = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253".decode("hex")
CBC_IV1 = CBC_CIPHER1[0:16]
CBC_IV2 = CBC_CIPHER2[0:16]

CTR_KEY = "36f18357be4dbd77f050515c73fcf9f2".decode("hex")
CTR_CIPHER1 = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329".decode("hex")
CTR_CIPHER2 = "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451".decode("hex")
CTR_IV1 = CTR_CIPHER1[0:16]
CTR_IV2 = CTR_CIPHER2[0:16]

aes_obj1 = AES.new(CBC_KEY, AES.MODE_CBC, CBC_IV1)
m1 = aes_obj1.decrypt(CBC_CIPHER1)[16:]

aes_obj2 = AES.new(CBC_KEY, AES.MODE_CBC, CBC_IV2)
m2 = aes_obj2.decrypt(CBC_CIPHER2)[16:]

ctr = Counter.new(128, initial_value=long(CTR_IV1.encode("hex"), 16)) #128, cause IV is 16 byte
aes_obj3 = AES.new(CTR_KEY, AES.MODE_CTR, CTR_IV1, counter=ctr)
m3 = aes_obj3.decrypt(CTR_CIPHER1[16:])

ctr = Counter.new(128, initial_value=long(CTR_IV2.encode("hex"),16))
aes_obj4 = AES.new(CTR_KEY, AES.MODE_CTR, CTR_IV2, counter=ctr)
m4 = aes_obj4.decrypt(CTR_CIPHER2[16:])

print "Message 1 (length " + str(len(CBC_CIPHER1)) + "): " + m1
print "Message 2 (length " + str(len(CBC_CIPHER2)) + "): " + m2
print "Message 3 (length " + str(len(CTR_CIPHER1)) + "): " + m3
print "Message 4 (length " + str(len(CTR_CIPHER2)) + "): " + m4
