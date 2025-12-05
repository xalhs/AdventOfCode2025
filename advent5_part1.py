with open('input5.txt') as fin:
	range_list = []
	tot = 0
	for line in fin:
		if line == "\n":
			break
		line = line.rstrip("\n")
		[start,end] = line.split("-")
		range_list.append(range(int(start),int(end)+1))

	for line in fin:
		num = int(line.rstrip("\n"))
		if any(num in rang for rang in range_list):
			tot+= 1

	print(tot)
