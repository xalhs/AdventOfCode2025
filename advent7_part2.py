with open('input7.txt') as fin:
    tot = 0
    list1 = []

    for i,line in enumerate(fin):
        line = line.rstrip("\n")
        list1.append(line)
        if "S" in line:
            starting_coord = [i, line.find("S")]

    coords_list = {tuple(starting_coord):1}
    at_bottom = False
    import time
    while at_bottom == False:
        new_coord_list = {}
        for coord1 in coords_list:
            coord = list(coord1)
            if list1[coord[0]+1][coord[1]] == "^":
                if (coord[0]+1 , coord[1]-1) in new_coord_list:
                    new_coord_list[(coord[0]+1 , coord[1]-1)] += coords_list[coord1]
                else:
                    new_coord_list[(coord[0]+1 , coord[1]-1)] = coords_list[coord1]
                if (coord[0]+1 , coord[1]+1) in new_coord_list:
                    new_coord_list[(coord[0]+1 , coord[1]+1)] += coords_list[coord1]
                else:
                    new_coord_list[(coord[0]+1 , coord[1]+1)] = coords_list[coord1]

            else:
                if (coord[0]+1 , coord[1]) in new_coord_list:
                    new_coord_list[(coord[0]+1 , coord[1])] += coords_list[coord1]
                else:
                    new_coord_list[(coord[0]+1 , coord[1])] = coords_list[coord1]
        if coord[0]+1 == len(list1)-1:
            at_bottom = True
        coords_list = new_coord_list
        
    for key in coords_list:
        tot += coords_list[key]
    print(tot)
