# list=[1,4,9,25,36,49,64,81,100]

# for num in list:
#     print(num)


list=[1,4,9,25,36,49,64,81,100]
idx=0
x=49
for el in list:
    if(el ==x):
        print("found at idx:",idx)
        # break
    else:
        print("not found")
        idx+=1    
 