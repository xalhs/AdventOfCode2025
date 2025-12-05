with open('input5.txt') as fin:
	range_dict= {}
	tot = 0
	start_list = []
	for line in fin:
		flag = False
		if line == "\n":
			break
		line = line.rstrip("\n")
		[start,end] = line.split("-")
		start = int(start)
		end = int(end)
		if start in range_dict:
			range_dict[start] = max(end , range_dict[start])
		else:
			range_dict[start] = end
			start_list.append(start)

	start_list.sort()
	dict2 = {}
	count = 0
	last_entry = 0
	for i,start in enumerate(start_list):
		if i>=1 and start <= dict2[last_entry] and dict2[last_entry]<=range_dict[start]:

		elif i>= 1 and start <= dict2[last_entry] and range_dict[start]< dict2[last_entry]:
			pass
		else:
			dict2[start] = range_dict[start]
			last_entry = start

	for start in dict2:
		tot+= dict2[start] - start + 1

	print(tot)
