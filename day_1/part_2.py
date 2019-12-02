def fuel_required(n):
   return max(n//3 - 2,0)

def compute(s):
    total=0
    for line in s:
        prev = int(line.strip())
        while prev > 0:
            prev = fuel_required(prev)
            total += prev
    return total

with open('input.txt') as f:
    print(compute(f))
        
