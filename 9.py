with open("9_input.txt","r") as f:
    X = f.read().rstrip("\n")
	
def encode(X):
    return [(i//2,int(item)) if i%2==0 else (-1,int(item)) for i,item in enumerate(X)]
    
    
L = encode(X)
reversed_result = []
while len(L) >0:
    item = L.pop()
    if item[0]<0:
        reversed_result.append(item)
        continue
    swapped = False
    for i,t in enumerate(L):
        if t[0]<0 and item[1] <= t[1]:
            consumed_mem = (-1,item[1])
            reversed_result.append(consumed_mem)
            left_over_mem_inplace = (-1,t[1] - item[1])
            #del(L[i])
            L[i] = left_over_mem_inplace
            L.insert(i,item)
            swapped = True
            break
    if swapped:
        pass
    else:
        reversed_result.append(item)
        

# def display(L):
    # res = ""
    # for id_num,repeats in L:
        # if id_num < 0:
            # string = repeats*"."
        # else:
            # string = repeats*str(id_num)
        # res+= string
    # return res 

# y = display(reversed(reversed_result))
checksum = 0
idx = 0
for id_num,repeats in reversed(reversed_result):
    if id_num < 0:
        pass
    else:
        checksum += id_num*sum([i for i in range(idx,idx+repeats)])
    idx+=repeats