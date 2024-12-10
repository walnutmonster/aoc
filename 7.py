with open("7_input.txt","r") as f:
    X = f.readlines()
ctr = 0
idxs_true = []
import math


    
for row,l in enumerate(X):
    print(math.floor(100*row/len(X)))
    n = int(l.split(":")[0])
    nums = [int(x) for x in l.split(":")[1].split(" ") if x!=""]
    n_gaps = len(nums)-1
    for i in range(2**n_gaps):
        s = bin(i)
        ops = "0"*(n_gaps-(len(s)-2))+s[2:]
        exponent_cutoff = int(math.ceil(math.log(n,2)))
        broken = False
        total = nums[0]
        for j,op in enumerate(ops):
            if op == "0":
                total = total+nums[j+1]
            elif op == "1":
                total = total*nums[j+1]
        if total == n:
            ctr+=n
            idxs_true.append(row)
            break

ctr2 = 0
import math
idxs_true_2 = []
def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

for idx,l in enumerate(X):
    if idx in idxs_true:
        continue
    print(math.floor(100*idx/len(idxs_true)))
    n = int(l.split(":")[0])
    nums = [int(x) for x in l.split(":")[1].split(" ") if x!=""]
    n_gaps = len(nums)-1
    for i in range(3**n_gaps):
        s = ternary(i)
        ops = "0"*(n_gaps-len(s))+s
        total = nums[0]
        for j,op in enumerate(ops):
            if op == "0":
                total = total+nums[j+1]
            elif op == "1":
                total = total*nums[j+1]
            elif op == "2":
                total = 10**len(str(nums[j+1]))*total+nums[j+1]
        if total == n:
            ctr2+=n
            idxs_true_2.append(idx)
            break



# with open("7_input.txt","r") as f:
    # X = f.readlines()
# ctr = 0
# idxs_true = []
# import math


    
# for row,l in enumerate(X):
    # print(math.floor(100*row/len(X)))
    # n = int(l.split(":")[0])
    # nums = [int(x) for x in l.split(":")[1].split(" ") if x!=""]
    # n_gaps = len(nums)-1
    # for i in range(2**n_gaps):
        # s = bin(i)
        # ops = "0"*(n_gaps-(len(s)-2))+s[2:]
        # ops = ops.replace("0","+").replace("1","*")
        # exponent_cutoff = int(math.ceil(math.log(n,2)))
        # broken = False
        # for exponent in range(1,exponent_cutoff+1):
            # total = nums[0]%2**exponent
            # for j,op in enumerate(ops):
                
                
                # total = eval(f"(total{op}{nums[j+1]})%2**{exponent}")
                
            # if total % 2**exponent!= n%2**exponent:
                # broken = True
                # break
        # if not broken:
            # ctr+=n
            # idxs_true.append(row)
            # break


# ctr2 = 0
# import math

# def ternary (n):
    # if n == 0:
        # return '0'
    # nums = []
    # while n:
        # n, r = divmod(n, 3)
        # nums.append(str(r))
    # return ''.join(reversed(nums))

# for idx,l in enumerate(X):
    # if idx in idxs_true:
        # continue
    # print(math.floor(100*row/len(X)))
    # n = int(l.split(":")[0])
    # nums = [int(x) for x in l.split(":")[1].split(" ") if x!=""]
    # n_gaps = len(nums)-1
    # for i in range(3**n_gaps):
        # s = ternary(i)
        # ops = "0"*(n_gaps-len(s))+s
        # ops = ops.replace("0","+").replace("1","*")
        # exponent_cutoff = int(math.ceil(math.log(n,2)))
        # broken = False
        # for exponent in range(1,exponent_cutoff+1):
            # total = nums[0]%2**exponent
            # for j,op in enumerate(ops):
                # a,b = total, nums[j+1]
                # if op =="2":
                    # total = eval(f"(10**len('{b}')*{a}+{b})%2**{exponent}")
                # else:
                    # total = eval(f"(total{op}{nums[j+1]})%2**{exponent}")
                
            # if total % 2**exponent!= n%2**exponent:
                # broken = True
                # break
        # if not broken:
            # ctr2+=n
            # break