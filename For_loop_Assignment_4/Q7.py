#WAP to print the positive numbers from a given range.
start=int(input("Enter Start of range : "))
End=int(input("Enter end of range : "))
for i in range(start,End):
    if(i > 0):
        print(i,end=" ")