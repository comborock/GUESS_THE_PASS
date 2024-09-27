import string
high = string.ascii_lowercase
#abcdefghijklmnopqrstuvwxyz
high_and_low = "bdfghjklpqty"
high_let = list("bdfhklt")
low_let = list("gjpqy")
middle_let = list("aceimnorsuvwxz")
HIGH_LET = string.ascii_uppercase
NUM = string.digits
SYM = string.punctuation

#Legend:
# H - high letters
# L - low letters
# M - middle letters ("i" is questionable)
# C - capital letters
# N - digits
# S - other ascii symbols

string = input("PUT IN TEXT:")
str2 = ""
for i in string:
    if i in high_let:
        str2 += "H"
    if i in low_let:
        str2 += "L"
    if i in middle_let:
        str2 += "M"
    if i in HIGH_LET:
        str2 += "C"
    if i in NUM:
        str2 += "N"
    if i in SYM:
        str2 += "S"
print(str2)
