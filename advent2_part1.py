with open('input2.txt') as fin:
	def is_repeating(num):
		num = str(num)
		dig = len(num)
		if dig %2 ==0:
			str1 = num[:int(dig/2)]
			if num == str1*2:
				return True
			
			

	tot = 0
	for line in fin:
		line= line.rstrip("\n")
		ranges = line.split(",")
		for id_range in ranges:
			[start,end] = id_range.split("-")
			start = int(start)
			end = int(end)
			for num in range(start , end+1):
				if is_repeating(num):
					tot+=num
	print(tot)					
	

