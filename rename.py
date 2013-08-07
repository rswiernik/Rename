import sys

oldVar = []
newVar = []

with open(sys.argv[1], 'r') as f:
	for line in f.readlines():
		try:
			#index = to find if there is a comparison, if not, skip
			line.index('=')
			#check if the choosen line is a comment line
			if (line.strip().startswith('//') is False):
				line = line.replace(' ', '')
				line = line.replace('\n','')
				varis = line.split('=')
				oldVar.append(varis[0])
				newVar.append(varis[1])
		except ValueError:
			continue

totalReplacements = 0

for i in range(2,len(sys.argv)):
	with open(sys.argv[i], 'r') as f:
		newlines = []
		for line in f.readlines():
			for x in oldVar:
				#print "[" + x + "],[" + newVar[oldVar.index(x)] + "]"
				oldline = line
				line = line.replace(x,newVar[oldVar.index(x)])
				if(oldline != line):
					totalReplacements += 1
			newlines.append(line)

	with open(sys.argv[i], 'w') as f:
		for line in newlines:
			f.write(line)

print str(totalReplacements) + " total replacements were made."