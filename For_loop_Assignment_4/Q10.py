#WAP to calculate and print the product of thecount of odd numbers a given range.
Count=0
K=1
start=int(input("Enter Start of range : "))
End=int(input("Enter end of range : "))
for i in range(start,End+1):
    if(i%2!=0):
        Count+=i
        K= K*i
print(K)