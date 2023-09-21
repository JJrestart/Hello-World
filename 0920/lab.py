count=0
for num in range(1,101):
    if(num%7==0) :
        print(num, end='\t')
        count+=1
        if (count%5==0) :
            print()
print()