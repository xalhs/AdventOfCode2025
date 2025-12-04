def at_count(map,i,j):
	count = 0
	for k in range(-1,2):
		for l in range(-1,2):
			if k ==0  and l ==0:
				continue
			if map[i+k][j+l] == "@":
				count +=1
	return count

with open('input4.txt') as fin:
	tot = 0
	map = [""]
	for line in fin:
		map.append("."+line)

	map[0] = "."*len(map[1])
	map.append("."*len(map[1]))

	for i,line in enumerate(map):
		for j,char in enumerate(line):
			if char == "@":
				if at_count(map,i,j) <4:
					tot +=1

	print(tot)
