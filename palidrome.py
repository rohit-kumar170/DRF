arr=[121,1,34,1991,6565775]
palidrome_list=[]
for i in range(len(arr)):
    new_str=str(arr[i])
    print(new_str)
    print(new_str[::-1])
    if new_str==new_str[::-1]:
        palidrome_list.append(new_str)
print(new_str)