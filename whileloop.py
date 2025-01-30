# q1
# i=1
# while i <=100:
#     print(i)
#     i+=1

# i=100
# while i>=1:
#     print(i)
#     i-=1


# n=int(input("enter the number:"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

# num=[1,4,9,16,25,36,49,64,81,100]

# i=0

# while i< len(num):
#     print(num[i])
#     i+=1


num=[1,4,9,16,25,36,49,64,81,100]
x=int(input("enter your index num:"))
i=0

while i<len(num):
    if (num[i]==x):
        print("found at index:",i)
        break    #stops th loop when it gets thr finding value.
    else:
        print("still finding")    
    i+=1
print("end of loop") 