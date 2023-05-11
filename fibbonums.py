num=int(input("Enter the range number: "))
i=0
a=0
b=1
while(i<num):
    if(i<=1):
        c=i
    else:
        c=a+b
        a=b
        b=c
    print(c)
    i=i+1
