if __name__=="main": 
    N = int(input)
    list = []
    for i in range(0,N): 
        value = input()
        pak_value = value.split()
        if pak_value[0]=="insert":
            e = int(pak_value[1])
            i = int(pak_value[2])
            list.insert(e,i)
        if pak_value[0]=="print":
            print(list)
        if pak_value[0]=="append": 
            e = int[pak_value[1]]
            list.append(e)
        if pak_value[0]=="sort": 
            list.sort()
        if pak_value[0]=="pop":
            list.pop()
        if pak_value[0]=="remove":
            e = int(pak_value[1])
            list.remove(e)
        if pak_value=="reverse":
            list.reverse()
            
