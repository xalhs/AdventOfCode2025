with open('input3.txt') as fin:
	tot = 0
	for line in fin:
		line= line.rstrip("\n")
		max_dig = 0
		max_i = 0
		for i,digit in enumerate(line[:-1]):
			if int(digit) > max_dig:
				max_dig = int(digit)
				max_i = i
				
		max_dig2 = 0
		for digit2 in line[max_i+1:]:
			if int(digit2) > max_dig2:
				max_dig2 = int(digit2)
		
		
		num = int(str(max_dig)+str(max_dig2))	
		tot+=num
	print(tot)					
	

