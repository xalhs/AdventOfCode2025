with open('input11.txt') as fin:
	tot = 0
	forwards_dic = {}
	paths = {}
	for line in fin:
		line = line.rstrip("\n")
		input = line.split(": ")[0]
		output = line.split(": ")[1].split(" ")
		forwards_dic[input] = output

	def find_paths(input,final):
		if input == final:
			return 1
		if (input,final) in paths:
			return paths[(input,final)]
		count = 0
		if input in forwards_dic:
			for output in forwards_dic[input]:
				count += find_paths(output , final)

		paths[(input,final)] = count
		return count

	print(find_paths("svr" , "fft")*find_paths("fft" , "dac")*find_paths("dac" , "out"))
