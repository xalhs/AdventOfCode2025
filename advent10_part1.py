with open('input10.txt') as fin:
	tot = 0
	for line in fin:
		config = line.split("[")[1].split("]")[0]
		config = config.replace("#" , "1").replace("." , "0")
		config = [int(i) for i,x in enumerate(config) if x == "1"]
		config = set(config)
		buttons = []
		#print(10)
		for i,but in enumerate(line.split("(")[1:]):
			#buttons = buttons.row_insert(i , Matrix([[0]*len(config)]))
			new_but = [int(x) for x in but.split(")")[0].split(",")]
			new_vec = [[0]*len(config)]
			buttons.append(new_but)
			#for but1 in new_but:
			#	new_vec += eye(len(config)).row(but1)
			
			#buttons = buttons.row_insert(i , new_vec)	
			
				
			#buttons.append([int(x) for x in but.split(")")[0].split(",")])
		
		min_but = float('inf')	
		for i in range(2**(len(buttons))):
			button_config = []
			cur_but = 0
			str1 = bin(i)[2:]
			if len(str1) < len(bin(2**(len(buttons))-1)[2:]):
				str1 = "0"*(len(bin(2**(len(buttons))-1)[2:])-len(str1)) + str1
				
			for j,digit in enumerate(str1):
				if digit == "1":
					cur_but +=1
					button_config += buttons[j]
		
			new_set = set()
			for item in set(button_config):
				if button_config.count(item)%2 !=0:
					new_set.add(item)
			
			if new_set == config:
				if cur_but < min_but:
					min_but = cur_but
					
			
		
		tot += min_but					
	
	print(tot)		
			

