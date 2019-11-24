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

def letterfreq(li):
    """Finds the letter frequency of a list of capital ordinals"""
    chartally,i = listmaker(26),0
    while i<len(li):
        chartally[li[i]-65] += 1
        i+=1
    return chartally

def topletters(chartally,n):
    """Sorts the character tally by most used letters"""
    i=0
    litop=chartally
    while i<n: #how many times you do it
        a,b,j=0,0,0
        while j<len(litop): #comb through list
            if litop[j]>a:
                a,b=litop[j],j
            j+=1
        print(chr(b+65),":",a," // ",end='')
        if i%6==5:
            print("\n")
        litop[b]=0
        i+=1
    print("\n")

def listmaker(n):
    """Make a list of size n containing zeros"""
    li,i=[],0
    while i<n:
        li+=[0]
        i+=1
    return li
    

def bigram(li):
    """Count ALL 26^2 possible bigrams.
    AA=bigram(0,0), AB=bigram(0,1) BA=bigram(1,0), etc."""
    bgnum=listmaker(676)
    i=0 #i = first letter
    while i<26:
        j=0 #j = second letter
        while j<26:
            k=0 #k = position on list
            while k<len(li)-1:
                if li[k]-65==i:
                    if li[k+1]-65==j: #element may not exist
                        bgnum[26*i+j]+=1
                k+=1
            j+=1
        i+=1
    return bgnum

def topn(n,li):
    """Top n bigrams"""
    i=0
    litop=li
    while i<n: #how many times you do it
        a,b,j=0,0,0
        while j<len(litop): #comb through list
            if litop[j]>a:
                a,b=litop[j],j
            j+=1
        print(chr(b//26+65),chr(b%26+65),":",a," // ",end='')
        if i%5==4:
            print("\n")
        litop[b]=0
        i+=1
            

def labelchartally(chartally):
    """Prints the character frequency list in alphabetical order"""
    i=0
    while i<len(chartally):
        print(chr(i+65),':',chartally[i],' / ',end='')
        if i%7==6:
            print("\n")
        i+=1
    print("\n")

def spacer(s,n):
    """Inserts a space into a string every n characters"""
    s = " ".join(s[i:i+n] for i in range (0, len(s), n))
    return s

def trigram_find(li):
    """Count ALL 26^3 possible trigrams.
    AAA=bigram(0,0,0), AAB=bigram(0,0,1) BAA=bigram(1,0,0), etc."""
    tgnum=listmaker(26**3)
    i=0 #i = first letter
    while i<26:
        j=0 #j = second letter
        while j<26:
            l=0 #l = third letter
            while l<26:
                k=0 #k = position on list
                while k<len(li)-2:
                    if li[k]-65==i:
                        if li[k+1]-65==j:
                            if li[k+2]-65==l:
                                tgnum[(26**2)*i+26*j+l]+=1
                    k+=1
                l+=1
            j+=1
        i+=1
    return tgnum

def topntrig(n,li):
    """Top n trigrams"""
    i=0
    litop=li
    while i<n: #how many times you do it
        a,b,j=0,0,0
        while j<len(litop): #comb through list
            if litop[j]>a:
                a,b=litop[j],j
            j+=1
        x,y,z = b//(26**2)+65,((b//26)%26)+65,b%26+65
        print(chr(x),chr(y),chr(z),":",a," / ",end='')
        if i%5==4:
            print("\n")
        litop[b]=0
        i+=1

def trigram(msg):
    li = msg2li(msg)
    tgnum = trigram_find(li)
    topntrig(10,tgnum)

def encryption(msg,key):
    """Takes strings msg and key and encrypts"""
    li=unreader(msg)
    k=unreader(key)
    print(k)
    i=0
    while i<26:
        j=0
        while j<len(li):
            if li[j]==i+65:
                li[j]=k[i]+32
            j+=1
        i+=1
    li=capitalize(li)
    li=backtoascii(li)
    result=tostring(li)
    return result

def getinfo(message):
    """Master program to get all pertinent info on a string"""
    li = msg2li(message)
    chartally = letterfreq(li)
    labelchartally(chartally)
    print('Letters ordered by frequency:')
    topletters(chartally,26)
    k=25 #change this value to change the number of bigrams reported
    print('Top',k,'bigrams:')
    bgnum=bigram(li)
    topn(25,bgnum)
    print("Length = ",len(li)) #comment this out to remove message length
    result = li2MSG(li)
    result = spacer(result,5) #comment this out to remove spaces
    return result

