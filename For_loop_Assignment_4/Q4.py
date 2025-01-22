#WAP to print all the ASCII values from a given character range.
#input : enter the  start of range:1
 #       enter the end of range:-2
  #  output:Wrong Input
  #Start=65
  #Ent=67
   # The Character of ASCII value 65 is A
   # The Character of ASCII value 66 is B
   # The Character of ASCII value 67 is C
   # ..
   # ..
   # ..
   # # The Character of ASCII value 89 is Y
    
Start =int(input("Enter the start of range : "))
End= int(input("Enter end of range : "))
if(Start<End):
    for i in range(Start,End):
        print("The character of ASCII value {} is {}".format(i,(chr(i))))
else:
    print("Wrong input")