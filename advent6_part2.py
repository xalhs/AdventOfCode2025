with open('input6.txt') as fin:
    tot = 0
    list1 = []
    for line in fin:
        line = line.rstrip("\n")
        list1.append(line)

    space_list = [-1]

    for i,char in enumerate(list1[0]):
        if char == " ":
            check = True
            for line in list1:
                if line[i] != " ":
                    check = False
            if check == True:
                space_list.append(i)
    space_list.append(len(list1[0])+1)
    aligned_list = []

    for i,line in enumerate(list1):
        aligned_list.append([])
        for j,space in enumerate(space_list[:-1]):
            aligned_list[i].append(line[(space_list[j]+1):space_list[j+1]])

    tot_list = []
    aligned_list.reverse()
    op = aligned_list.pop(0)
    op = "".join(op)
    op = op.split()
    true_list = []
    true_list = [[None]*len(aligned_list) for i in range(len(aligned_list[0]))]

    for i in range(len(aligned_list)):
        for j in range(len(aligned_list[i])):
            true_list[j][i] = aligned_list[i][j]

    for j,problem in enumerate(true_list):
        true_set = []
        for i in range(len(problem[0])):
            true_set.append("")
            for num in problem:
                if len(num)>i:
                    true_set[i] +=num[i]
        true_set = [int(x.split()[0][::-1]) for x in true_set]
        if op[j] == "*":
            temp = 1
            for num1 in true_set:
                temp *= num1
            tot+= temp
        elif op[j] == "+":
            tot += sum(true_set)

    print(tot)
