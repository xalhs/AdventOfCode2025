def in_basis(vec):
	if 1 not in vec:
		return False
	vec1 = list(vec)
	vec1.pop(vec1.index(1))
	if vec1 == [0]*len(vec1):
		return True
	else:
		return False

def split_matrix(mat, config):   #Separates invertible from non-invertible part of the matrix
    n = len(mat.col(0))
    n2 = len(mat.row(0))
    basis = []
    for i in range(n2):
        basis.append(eye(n,n2).col(i))
    separating = True
    while separating:
        separating = False
        for nullvec in (mat.T).nullspace():
            if in_basis(nullvec):
                continue
            else:
                separating = True
                denom = 1
                max_el = 0
                for comp in nullvec:
                    denom = lcm(denom , comp.q)
                    if abs(comp) > max_el:
                        max_el = abs(comp)
                nullvec = denom*nullvec
                if denom == 1:
                    glob_com_div = max_el
                    for comp in nullvec:
                        glob_com_div = gcd(glob_com_div , comp)
                    nullvec = nullvec / glob_com_div
                last_comp = 0
                init_index = n
                for i , comp in reversed(list(enumerate(nullvec))):
                    if last_comp ==0:
                        last_comp = -comp
                        init_index = i
                    else:
                        if comp == 0:
                            continue
                        while comp%last_comp != 0:  #n = last_comp
                            if last_comp == comp:  #m = comp
                                K2(mat ,config, init_index , i , False)
                                comp -= last_comp
                            elif last_comp == -comp:
                                K2(mat ,config, init_index , i , True)
                                comp += last_comp
                            elif abs(comp) > abs(last_comp):
                                if comp*last_comp>0:
                                    comp -= last_comp
                                    K2(mat ,config, init_index , i , False)
                                else:
                                    comp += last_comp
                                    K2(mat ,config, init_index , i)
                            elif abs(comp) < abs(last_comp):
                                if comp*last_comp>0:
                                    last_comp -= comp
                                    K2(mat ,config, i , init_index , False)
                                else:
                                    last_comp += comp
                                    K2(mat ,config, i , init_index)
                        ratio = abs(int(comp / last_comp))
                        for j in range(ratio):
                            if comp*last_comp > 0:
                                comp -= last_comp
                                K2(mat ,config, init_index , i , False)
                            else:
                                comp += last_comp
                                K2(mat ,config, init_index , i)
            break
    dim_nul = len((mat.T).nullspace())
    for i in range(dim_nul):
        for j in range(len(mat.col(0))):
            if list(mat.row(j)) == [0]*len(list(mat.row(j))):
                mat.row_del(j )
                config.row_del(j)
                break

    return [mat,config]

with open('input10og.txt') as fin:
	from sympy import *
	from itertools import chain, combinations, product
	import copy
	def K2(K , vec, n , m , plus = True):
		if n == m:
			raise("whaterror " + str(n) + " " + str(m))
		if plus == False:
			mult = -1
		else:
			mult = 1
		K[n,:] += mult*K[m,:]
		vec[n] += mult*vec[m]

	tot = 0
	for line in fin:
		config = line.split("{")[1].split("}")[0]
		config = Matrix([int(x) for x in config.split(",")])
		size = len(config)
		buttons = Matrix()
		buttons = []
		for i,but in enumerate(line.split("(")[1:]):
			new_but = [int(x) for x in but.split(")")[0].split(",")]
			new_vec = Matrix([[0]*len(config)])

			for but1 in new_but:
				new_vec += eye(len(config)).row(but1)

			buttons.append(new_vec)

		extra_count = 0
		smallest_press = float('inf')
		red_rows = []
		buttons = Matrix(buttons).T
		removing_redundances = True
		while removing_redundances and list(buttons)!= []:
			removing_redundances = False
			for i in range(len(buttons.col(0))):
				if in_basis(buttons[i,:]):
					extra_count += config[i]
					config-= buttons.col(list(buttons.row(i)).index(1))*config[i]
					buttons.col_del(list(buttons.row(i)).index(1))
					buttons.row_del(i)
					config.row_del(i)
					removing_redundances = True
					size -=1
					break

		if list(buttons) == []:
			tot+= extra_count
			continue

		buttons = [buttons.T[i,:] for i in range(len(buttons.row(0)))]
		old_buttons = copy.deepcopy(buttons)
		buttons = Matrix(buttons).T
		[buttons,config] = split_matrix(buttons,config)
		min_list = []
		for i in range(len(buttons.row(0))):
			min_list.append(min([config[j] for j in range(len(buttons.col(i))) if buttons[j,i] ==1]) )
		c = copy.deepcopy(min_list)
		c.sort()
		if (smallest_press == float('inf') or True):
			size = len(config)
			dif = len(old_buttons) - size
			old_buttons = buttons
			if dif >=0:
				sequence = []
				for i in range(len(old_buttons.row(0))):
					sequence.append(i)
					old_buttons.col_swap(i , min_list[i:].index(c[i])+i)
					min_list  = Matrix(min_list)
					min_list.row_swap(i , min_list[i:].index(c[i])+i)
					min_list = list(min_list)

				for comb1 in combinations( sequence, dif):
					M = Matrix()
					initial = Matrix()
					iter_list = []
					comb1 = list(comb1)
					prev_item = 0
					for item in comb1:
						M = Matrix.hstack(M, old_buttons[: , prev_item:item])
						prev_item = item+1
						initial = Matrix.hstack(initial , old_buttons[: , item:(item+1)] )
						iter_list += c[item:(item+1)]

					M = Matrix.hstack(M, old_buttons[: , (prev_item):])
					if det(M) != 0:
						break

				if dif == 0:
					initial = 0

				if det(M) !=0:
					for a in product(*tuple([range(x+1) for x in iter_list])):
						if list(a) == []:
							a = Matrix(len(config) , 1 , [0]*len(config))
						new_con = config - initial*Matrix(a)
						new_config = M**-1*new_con
						for l,k in enumerate(comb1):
							new_config = new_config.row_insert(k , Matrix([a[l]]))
						if all((int(el) == el and el>=0 for el in new_config)):
							if Matrix(old_buttons)*new_config == config:
								presses = sum(new_config)
								if presses < smallest_press:
									smallest_press = presses
									smallest_new_conf = new_config

		if smallest_press == float('inf'):
			sym = buttons.T*buttons
			if det(sym)!= 0:
				new_config = sym**-1*buttons.T*config
				if buttons*new_config == config:
					presses = sum(new_config)
					if presses < smallest_press:
						smallest_press = presses
						smallest_new_conf = new_config

		smallest_press += extra_count
		tot += smallest_press

	print(tot)
