with open('input6.txt') as fin:
    tot = 0
    list1 = []
    for line in fin:
        line = line.rstrip("\n")
        try:
            list1.append([int(x) for x in line.split()])
        except:
            list1.append(line.split())
    tot_list = []
    list1.reverse()
    op = list1.pop(0)
    tot_list = list1.pop(0)
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            if op[j] == "*":
                tot_list[j]*= list1[i][j]
            elif op[j] == "+":
                tot_list[j]+= list1[i][j]
    tot = sum(tot_list)
    print(tot)
