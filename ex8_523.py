s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'	
dad = {}							
for i, j in enumerate(s):			
    dad[j] = i	

def string_to_num(x):				
    mom = []							
    mom+=x								
    for i, k in enumerate(x):			
            mom[i] = dad[k]				
    return mom							
				
    
   