with open ('input.txt') as f:
    mass = [(int(line.strip())//3)-2 for line in f]

print (sum(mass))
    
