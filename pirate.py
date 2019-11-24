print("Feed me yer' string, matey. (or 'ctrl-Z' to abort)")
pirate_story = input();			
while True:
	print("Go on an type a letter in to replace (or 'ctrl-Z' to abort).")
	a = input()
	print("And to replace it with: (or 'ctrl-Z' to abort).")
	b = input()
	print("And here's the new string (or 'ctrl-Z' to abort)")
	pirate_story = pirate_story.replace(a,b)
	pirate_space = " ".join(pirate_story[i:i+5] for i in range (0, len(pirate_story), 5))
	print(pirate_space)