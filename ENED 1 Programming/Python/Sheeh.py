#for x in ("1","2","3","4","5","6","7","8","9","10"):
#    print(x)
#print("We have 4 even numbers and 6 odd numbers")
even = 0
for ix in range(11):
    print(ix)
#if ix is even add 1 to even
    if ix % 2 == 0:
        even = even + 1
print("We have "+str(even)+" odd numbers and "+str(10-even)+" even numbers")
    
   