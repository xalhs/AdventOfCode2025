with open('input2.txt') as fin:
	def is_repeating(num):
		num = str(num)
		dig = len(num)
		if dig == 1:
			return
		for div in get_divisors(dig):
			str1 = num[:div]
			if num == str1*int((dig/div)):
				return True
	
	def get_divisors(num):
		divs=[1]
		i = 2
		while i <= sqrt(num):
			if gcd(i,num) == i:
				divs.append(i)
				if int(num/i) not in divs:
					divs.append(int(num/i))
			i+=1	
		return divs	
	from math import *
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
	

