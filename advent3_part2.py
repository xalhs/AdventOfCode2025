with open('input3.txt') as fin:
	tot = 0
	for line in fin:
		line= line.rstrip("\n")
		max_dig = [0]*12
		max_i = [0]*13
		for j in range(1,13):
			for i,digit in enumerate(line):
			#enumerate(line[max_i[j-1]:-(12-j+1)]):
				if i>= max_i[j-1] and i<len(line)-(12-j):
					if int(digit) > max_dig[j-1]:
						max_dig[j-1] = int(digit)
						max_i[j] = i+1
		num_str = ""
		for dig in max_dig:
			num_str += str(dig)		
		num = int(num_str)	
		tot+=num
	print(tot)					
	

