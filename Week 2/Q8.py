"""

Recall that encryption systems do not fully hide the length of transmitted messages. Leaking the length of web requests has been used to eavesdrop on encrypted HTTPS traffic to a number of web sites, such as tax preparation sites, Google searches, and healthcare sites. Suppose an attacker intercepts a packet where he knows that the packet payload is encrypted using AES in CBC mode with a random IV. The encrypted packet payload is 128 bytes. Which of the following messages is plausibly the decryption of the payload:

Solution: 

Length of message must be <= then 128byte - IV(16byte), but >= 128Byte - IV(16byte) - max padding(16byte)

"""

msgs = ["If qualified opinions incline to believe in the exponential conjecture, then I think we cannot afford not to make use of it.",
        "An enciphering-deciphering machine (in general outline) of my invention has been sent to your organization.",
        "To consider the resistance of an enciphering process to being broken we should assume that at same times the enemy knows everything but the key being used and to break it needs only discover the key from this information.",
        "We see immediately that one needs little information to begin to break down the process."]

maxBound = 128 - 16
minBound = 128 - 16 - 16
for ctr, msg in enumerate(msgs):
    if(len(msg) <= maxBound and len(msg) >= minBound):
        print "Message " + str(ctr+1) + "is the plain text, cause its length is: " + str(len(msg))
        print msg



