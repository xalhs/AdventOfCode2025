with open('input7.txt') as fin:
    tot = 0
    list1 = []

    for i,line in enumerate(fin):
        line = line.rstrip("\n")
        list1.append(line)
        if "S" in line:
            starting_coord = [i, line.find("S")]

    coords_list = [starting_coord]
    at_bottom = False
    import time
    while at_bottom == False:
        new_coord_set = set()
        for coord in coords_list:
            if list1[coord[0]+1][coord[1]] == "^":
                new_coord_set.add((coord[0]+1 , coord[1]-1))
                new_coord_set.add((coord[0]+1 , coord[1]+1))
                tot +=1
            else:
                new_coord_set.add((coord[0]+1 , coord[1]))
        if coord[0]+1 == len(list1)-1:
            at_bottom = True
        coords_list = [list(x) for x in new_coord_set]
    print(tot)
