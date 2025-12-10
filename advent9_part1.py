with open('input9.txt') as fin:

	coord_list =[]
	max_rec = 0
	for line in fin:
		line = line.rstrip("\n")
		coords = [int(x) for x in line.split(",")]
		for ref_coord in coord_list:
			rec = (abs(coords[1]-ref_coord[1])+1)*(abs(coords[0]-ref_coord[0])+1)
			if rec > max_rec:
				max_rec = rec
			
		coord_list.append(coords)	
		
	print(max_rec)
