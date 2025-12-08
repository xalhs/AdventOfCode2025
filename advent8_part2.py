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
			smallest_d.append(dist)
			d_dict[dist] = [i,j]
			
		coord_list.append(coords)	
		
	set_list = []
	smallest_d.sort()
	for dist in smallest_d: 
		pair = d_dict[dist]
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
		if len(set_list[0]) == len(coord_list):
			break				
			
	print(coord_list[pair[0]][0]*coord_list[pair[1]][0])			
		
			 
		 
