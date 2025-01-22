#WAP to print the number divisible by 7 but not divisible by 3 between 1 to 100.
start=int(input("Enter Start of range : "))
End=int(input("Enter end of range : "))
for i in range(start,End):
    if((i%7==0)and(i%3!=0)):
        print(i,end=" ")