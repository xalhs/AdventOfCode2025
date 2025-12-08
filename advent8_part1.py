with open('input8.txt') as fin:

	def calculate_distance(coord1 , coord2):
		s = 0
		for i in range(3):
			s+= (coord1[i]-coord2[i])**2
		return s	
			
	coord_list = []
	smallest_d = []
	d_dict = {}
	
	for i,line in enumerate(fin):
		line = line.rstrip("\n")
		coords = [int(x) for x in line.split(",")]
		for j,ref_coord in enumerate(coord_list):
			dist = calculate_distance(coords , ref_coord)
			if len(smallest_d) <1000:
				smallest_d.append(dist)
				if dist in d_dict:
					if not {coords,ref_coord} in d_dict[dist]:
						d_dict[dist].append({i,j})
				else:
					d_dict[dist] = [{i,j}]		
						
						
			else:
				if dist < smallest_d[-1]:
					smallest_d.pop(-1)
					smallest_d.append(dist)
					if dist in d_dict:
						if not {coords,ref_coord} in d_dict[dist]:
							d_dict[dist].append({i,j})
					else:
						d_dict[dist] = [{i,j}]
			smallest_d.sort()			
				
		coord_list.append(coords)
		
	set_list = []
	for dist in smallest_d:
		for pair in d_dict[dist]:
			ind1 = "x"
			ind2 = "x"
			pair = list(pair)
			for i,set1 in enumerate(set_list):
				if pair[0] in set1:
					ind1 = i
				if pair[1] in set1:
					ind2 = i
					
			if ind1 == "x":
				ind1 = len(set_list)
				set_list.append({pair[0]})
				
			if ind2 == "x":
				ind2 = len(set_list)
				set_list.append({pair[1]})
			
			if ind1 != ind2:	
				set1 = set_list.pop(max(ind1,ind2))
				set2 = set_list.pop(min(ind1,ind2))
				set_list.append(set1.union(set2))
					
	
	len_list = []
	for set1 in set_list:
		len_list.append(len(set1))
	
	len_list.sort()
	tot = len_list[-1]*len_list[-2]*len_list[-3]
	print(tot)			
				
		
		
			 
		 
