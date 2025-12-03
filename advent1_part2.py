with open('input1.txt') as fin:
	tot = 0
	pos = 50
	for line in fin:
		mult = 1
		if line.startswith("L"):
			mult = -1
			val = line.split("L")[1]
		else:
			val = line.split("R")[1]
		
		val = int(val)
		prev_pos = pos
		pos += mult*val
		tot += int(abs((pos - pos%100)/100))
		pos = pos%100
		
		
		
		if prev_pos ==0 and mult == -1:
			tot -=1
		if pos ==0 and mult == -1:
			tot+=1	
	print(tot)					
	

