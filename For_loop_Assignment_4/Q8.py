#WAP to print the number divisible by 5 and divisible by 3 in a given range.
start=int(input("Enter Start of range : "))
End=int(input("Enter end of range : "))
for i in range(start,End):
    if((i%3==0)and(i%5==0)):
        print(i,end=" ")