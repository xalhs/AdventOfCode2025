with open('input9.txt') as fin:

	unpack = []
	for line in fin:
		unpack.append(line)

	unpack.append(unpack[0])
	coord_list =[]
	boundary_list =[]
	bound_dict = {}

	for line in unpack:
		line = line.rstrip("\n")
		coords = [int(x) for x in line.split(",")]
		boundary_list.append(coords)
		if coord_list != []:
			if coord_list[-1][0] == coords[0]:
				if coords[1] > coord_list[-1][1]:
					if (coords[0] , coords[1]) in bound_dict:
						bound_dict[(coords[0] , coords[1])] += "D"

					else:
						bound_dict[(coords[0] , coords[1])] = "D"

					if (coord_list[-1][0] , coord_list[-1][1]) in bound_dict:
						bound_dict[(coord_list[-1][0] , coord_list[-1][1])] += "D"

					else:
						bound_dict[(coord_list[-1][0] , coord_list[-1][1])] = "D"

					for j in range(coord_list[-1][1]+1 ,coords[1] ):
						bound_dict[(coords[0] , j)] = "D"

				if coords[1] < coord_list[-1][1]:
					if (coords[0] , coords[1]) in bound_dict:
						bound_dict[(coords[0] , coords[1])] += "U"

					else:
						bound_dict[(coords[0] , coords[1])] = "U"

					if (coord_list[-1][0] , coord_list[-1][1]) in bound_dict:
						bound_dict[(coord_list[-1][0] , coord_list[-1][1])] += "U"

					else:
						bound_dict[(coord_list[-1][0] , coord_list[-1][1])] = "U"

					for j in range(coords[1]+1 , coord_list[-1][1]):
						bound_dict[(coords[0] , j)] = "U"

			if coord_list[-1][1] == coords[1]:
				if coords[0] > coord_list[-1][0]: #
					if (coords[0] , coords[1]) in bound_dict:
						bound_dict[(coords[0] , coords[1])] += "R"

					else:
						bound_dict[(coords[0] , coords[1])] = "R"

					if (coord_list[-1][0] , coord_list[-1][1]) in bound_dict:
						bound_dict[(coord_list[-1][0] , coord_list[-1][1])] += "R"

					else:
						bound_dict[(coord_list[-1][0] , coord_list[-1][1])] = "R"

					for j in range(coord_list[-1][0]+1 ,coords[0] ):
						bound_dict[(j , coords[1])] = "R"

				if coords[0] < coord_list[-1][0]:
					if (coords[0] , coords[1]) in bound_dict:
						bound_dict[(coords[0] , coords[1])] += "L"

					else:
						bound_dict[(coords[0] , coords[1])] = "L"

					if (coord_list[-1][0] , coord_list[-1][1]) in bound_dict:
						bound_dict[(coord_list[-1][0] , coord_list[-1][1])] += "L"

					else:
						bound_dict[(coord_list[-1][0] , coord_list[-1][1])] = "L"

					for j in range(coords[0]+1,coord_list[-1][0]):
						bound_dict[(j , coords[1])] = "L"

		coord_list.append(coords)

	max_rec = 0

	def classify_points(direction):
		if direction in ["DL", "LU", "UR", "RD"]:
			return "conv"
		if direction in ["DR", "RU", "UL", "LD"]:
			return "conc"

	def add_coords(coord1 , coord2):
		return [coord1[0]+coord2[0] , coord1[1]+coord2[1]]

	dir_dict = {"R":[1,0], "U":[0,-1] , "L":[-1,0] , "D":[0,1]}
	op_dir = {"R":"L" , "U":"D" , "D":"U", "L":"R"}
	clockwise_dir={"U":"R" , "R":"D" , "D":"L" , "L":"U"}

	def go_far(point, dir):
		while True:
			point = add_coords(point , dir_dict[dir])
			if tuple(point) in bound_dict:
				if clockwise_dir[dir] in bound_dict[tuple(point)]:
					return point

	box = {}

	def boxit(list1):
		hor_list =[]
		ver_list = []
		for coord in list1:
			hor_list.append(coord[0])
			ver_list.append(coord[1])
		return([range(min(hor_list),max(hor_list)+1)   ,range(min(ver_list) , max(ver_list)+1)])

	def inbox(base_coord, ref_coord):
		if ref_coord[0] in box[tuple(base_coord)][0] and ref_coord[1] in box[tuple(base_coord)][1]:
			return True
		else:
			return False

	def compatible(coord1,coord2):
		return inbox(coord1,coord2) and inbox(coord2,coord1)

	max_rec = 0
	for i,coords in enumerate(coord_list):
		list1 = [coords]

		if classify_points(bound_dict[tuple(coords)]) == "conv":
			cor1 = go_far(coords , op_dir[bound_dict[tuple(coords)][0]])
			cor2 =  (go_far(coords , bound_dict[tuple(coords)][1]))
			list1.append(cor1)
			list1.append(cor2)

		else:
			for dir in dir_dict:
				list1.append(go_far(coords , dir))

		box[tuple(coords)] = boxit(list1)
		for ref_coord in coord_list[:i]:
			if compatible(coords , ref_coord):
				rec = (abs(coords[1]-ref_coord[1])+1)*(abs(coords[0]-ref_coord[0])+1)
				if rec > max_rec:
					max_rec = rec

	print(max_rec)
