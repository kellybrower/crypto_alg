from sys import argv
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'	
code = {}							
for i, j in enumerate(s):			
        code[j] = i

def string_to_num(x):					
    nums = []							
    nums += x								
    for i, k in enumerate(x):			
            nums[i] = code[k]				
    return nums							

def caesar(x, d):					
    nums = string_to_num(x)
    for i in range(len(nums)):
            nums[i] = (nums[i] + d) % 26
    decode = {value:key for key, value in code.items()}
    for i, j in enumerate(nums):
            nums[i] = decode[j]
    t = str()
    for i in range(len(nums)):
    	t+=nums[i]
    return t