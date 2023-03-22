# Leetcode 271

# # Algorithm:
# Loop through the array to find each string. create a new string and add its length, a "#" sign and that string. 
# This way every string in the longer string is separated by its length, so we know how long it is 
# To decode: we loop through the string:
# till we find a "#" sign, we keep concatenating the characters before it to find the length
# we then slice the string from j+1 (character after # sign) to j+1+length (to the last character in the word) and append its string version to the return list.


# Code:
def encode(strs):
    newStr = ""
    for s in strs:
        length = len(s)
        newStr += str(length) + "#" + s
    return newStr

def decode(thisStr):
    res, i = [],0
    while i < (len(thisStr)):
        j = i
        while thisStr[j] != "#":
            j += 1
        length = int(thisStr[i:j])
        res.append(thisStr[j+1:j+1+length])
        i = j + length + 1
    return res

print(encode(["Aimen","Moten","is","Amazing", "Bye"]))
print(decode("5#Aimen5#Moten2#is7#Amazing3#Bye"))