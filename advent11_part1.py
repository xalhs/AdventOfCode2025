with open('input11.txt') as fin:
	tot = 0
	forwards_dic = {}
	paths_to_out = {}
	for line in fin:
		line = line.rstrip("\n")
		input = line.split(": ")[0]
		output = line.split(": ")[1].split(" ")
		forwards_dic[input] = output

	def find_paths_to_out(input):
		if input == "out":
			return 1
		if input in paths_to_out:
			return paths_to_out[input]
		count = 0
		for output in forwards_dic[input]:
			count += find_paths_to_out(output)

		paths_to_out[input] = count
		return count

	print(find_paths_to_out("you"))
