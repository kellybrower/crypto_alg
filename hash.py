astring = ['cat', 'dog', 'zebra', 'jesus']
tablesize = len(astring) # defining tablesize to be the number of elements in a table
def hash (astring, tablesize):
  sum = 0
  for pos in range (len(astring)): # for loop to iterate through set
          sum = sum + ord(astring[pos]) * len(astring[pos])
          return sum%tablesize

print tablesize
for string in astring:
    print hash(string, tablesize)
