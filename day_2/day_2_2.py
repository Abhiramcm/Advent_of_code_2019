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
def compute(s):
    for noun in range(100):
        for verb in range(100):
            temp = s[:]
            temp[1]=noun
            temp[2]=verb
            if program_assist(temp)==19690720:
                return 100*noun+verb
with open('input.txt') as f:
    m = f.read()
    lis = [int(part) for part in m.strip().split(',')]
    result = compute(lis)
print(result)
