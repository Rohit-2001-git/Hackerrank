N = int(input().strip())
list2=[]
for i in range(N):
    list1=input().strip().split(" ")
    if list1[0]=='insert'or'INSERT':
        k=int(list1[1])
        m=int(list1[2])
        list2.insert(k,m)
    elif list1[0]=='print' or 'PRINT':
        print(list2)
    elif list1[0]=='remove'or'REMOVE':
       list2.remove(int(list1[1]))
    elif list1[0]=='append'or'APPEND':
        list2.append(int(list1[1]))
    elif list1[0]=='sort'or'SORT':
        list2.sort()
    elif list1[0]=='pop'or'POP':
        list2.pop()
    elif list1[0]=='reverse'or'REVERSE':
        list2.reverse()
                
    
    
    

    