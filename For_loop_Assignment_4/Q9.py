#WAP to print the count of all negative numbers from a given range.
count=0
start=int(input("Enter Start of range : "))
End=int(input("Enter end of range : "))
for i in range(start,End+1):
    if(i < 0):
            count+=1
print(count)