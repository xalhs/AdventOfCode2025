with open('input12.txt') as fin:
    i = 0
    shapes = []
    shape_size = []
    tot = 0
    for line in fin:
        if line == "\n":
            shape_size.append(counter)
            i+=1
        elif "x" in line:
            size = [int(x) for x in line.split(":")[0].split("x")]
            quantities = [int(x) for x in line.rstrip("\n").split(": ")[1].split(" ")]
            total_size = 0
            max_size = 0
            for j,quantity in enumerate(quantities):
                total_size += quantity*shape_size[j]
                max_size += quantity*9
            if total_size > size[0]*size[1]:
                continue # boxes would not fit even if they were liquid
            elif max_size <= size[0]*size[1]:
                tot+=1  #boxes fit in their own 3x3 box and are still well within the total area
            else:
                print("Insert code to compute these cases")

        else:
            if ":" in line:
                counter = 0
                shapes.append([])
            else:
                counter += line.count("#")
                shapes[i].append(line.rstrip("\n"))

    print(tot)
