arr=[121,1,34,1991,6565775]
palidrome_list=[]
for num in arr:
    #print(num)
    rev=0
    temp=num
    while temp>0:
        dig=temp%10
        temp=temp//10
        rev=rev*10+dig
    if num==rev:
       palidrome_list.append(num)
print(palidrome_list) #palidrome list
print(max(palidrome_list))
       

