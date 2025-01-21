#write the program that determines whether a given input year is a leap year or not
year=int(input("Enter the year : "))
if((year%100==0 and year%400==0)or year%4==0):
    print("leap Year")
else:
    print("Not Leap Year")