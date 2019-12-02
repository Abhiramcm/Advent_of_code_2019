def program_assist(l):
    i=0
    while l[i]!=99:
       if l[i]==1:
           l[l[i+3]]=l[l[i+1]]+l[l[i+2]]
           i+=4 
       else:
        l[l[i+3]]=l[l[i+1]]*l[l[i+2]]
        i+=4 
    
        
    return l[0]
            
with open('input.txt') as f:
    m=f.read()
    lis = [int(part) for part in m.strip().split(',')]
    lis[1]=12
    lis[2]=2
    result = program_assist(lis)
print(result)
        
        
        
