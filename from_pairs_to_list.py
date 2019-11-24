li = list()

with open('sharif_pairs.txt') as f:
	content = f.readlines()
	
li = [x.strip() for x in content]
	