rawCryptedMessages = (
"e86d2de2e1387ae9",
"1792d21db645c008",
"4af532671351e2e1",
"87a40cfa8dd39154",
"7b50baab07640c3d",
"ac343a22cea46d60",
"9d1a4f78cb28d863",
"75e5e3ea773ec3e6"
)
 
def hexXor(msg1, msg2):
    str1 = msg1.decode("hex")
    str2 = msg2.decode("hex")
    strXor = "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(str1, str2)])
    return strXor.encode("hex")

for i in xrange(0, len(rawCryptedMessages), 2):
    print hexXor(rawCryptedMessages[i], rawCryptedMessages[i+1])
    
    
