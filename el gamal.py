import random
def expmod(a,k,m):
    """Computes a^k mod m"""
    b=1
    while k!=0:
        if k%2==1:
            b=(b*a)%m
        a,k=(a**2)%m, k//2
    return b

def unreader(message):
    """Converts a string of characters to a list of numbers"""
    li = [] #the list containing the converted message
    for i in message:
        li.append(ord(i))
    return li

def remover(li):
    """Removes non-letters from a list of ordinals"""
    i=0
    while i<len(li):
        if li[i]<65:
            del li[i]
            i-=1 #corrects for decreasing list size
        if li[i]>122:
            del li[i]
            i-=1 #corrects for decreasing list size
        if li[i] in (91,96):
            del li[i]
            i-=1 #corrects for decreasing list size
        i+=1
    return li

def capitalize(li):
    """Converts ordinals representing lower-case letters to upper-case"""
    i=0
    while i<len(li):
        if li[i]>91:
            li[i] -= 32
        i += 1
    return li

            
def backtoascii(li):
    """Converts ordinals back to ASCII"""
    i = 0
    while i<len(li):
        li[i] = chr(li[i])
        i+=1
    return li

def tostring(li):
    """Converts list to string"""
    result,i="",0
    while i<len(li):
        result += li[i]
        i += 1
    return result

def msg2li(message):
    """Master program to convert any string (including punctuation)
    into a list of capital ordinals"""
    li=unreader(message)
    li=remover(li)
    li=capitalize(li)
    return li

def li2MSG(li):
    """Master program to convert list of ordinals to an ASCII string"""
    li=backtoascii(li)
    result=tostring(li)
    return result

def smash(numList):
    """smashes a list of numbers into a single number"""
    s = ''.join(map(str, numList))
    return int(s)

def smashMSG(li):
    """Driver program that takes a string input then converts it to a long number"""
    return(int(smash(msg2li(li))))

def chunk(li,L):
    """Master program that makes blocks of length L suitable for encryption"""
    splitdigits = [int(i) for i in str(smashMSG(li))]
    Chunks_of_size_prime = [splitdigits[n:n+L] for n in range(0, len(splitdigits), L)]
    list2 = list(map(smash, Chunks_of_size_prime))
    return list2
    
def pubkeygen(P,a,s):
    """Generates public key p = prime, a = element of Z_p (primitive or not), b = a^s mod p, s is secret key"""
    b = expmod(a,s,P)  #do not share s! a does not need to be a primitive root!
    return [P,a,b] #public key

def encryptblock(a,b,blk,P):
    """Encrypts a block of El Gamal"""
    k = random.randrange(P-1)
    r = expmod(a,k,P)
    t = (expmod(b,k,P) * blk)%P
    return [r,t]

def decrypt(r,t,s,P):
    """Computes Decode with known secret key 's'"""
    return ((t*(expmod(r,((P-1)-s),P)) % P))

def encryptallblocks(P,a,s,message,L):
    """Encrypts all blocks and outputs them as a list of encryption pairs"""
    b = pubkeygen(P,a,s)[2]
    outlist = []
    for blocks in chunk(message,L):
        outlist.append(encryptblock(a,b,blocks,P))
    return outlist

def decryptallblocks(pairlist,s,P):
    """Decrypts all pairs of encoded messages with known secret key s"""
    decoded = []
    for sublist in pairlist:
        decoded.append(decrypt(sublist[0],sublist[1],s,P))
    return decoded
        
