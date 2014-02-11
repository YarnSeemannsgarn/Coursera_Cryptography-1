#!/usr/bin/python

# Coursera Crypto Homework Week 3
# Read movie byte by byte in reverse and hash every 1KB block
from Crypto.Hash import SHA256

# movie = open("/home/jan/Desktop/Cryptography 1/3_Week/6 - 2 - Generic birthday attack (16 min).mp4", "rb")
movie = open("/home/jan/Desktop/Cryptography 1/3_Week/6 - 1 - Introduction (11 min).mp4")

bytes_movie = []
bytes_block = movie.read(1024)
while bytes_block != "":
    bytes_movie.append(bytes_block)
    bytes_block = movie.read(1024)
movie.close()

# Last block
hi = ""

# Middle blocks
for bytes_block in reversed(bytes_movie):
    h = SHA256.new()
    h.update(bytes_block + hi)
    hi = h.digest()

# Last block
print hi.encode("hex")

#correct_h0 = "03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8"
