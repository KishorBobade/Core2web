#WAP to print all the ASCII values from a given character range.
#input : enter the  start of range:A
 #       enter the end of range:Z
  #  output:ASCII Value A is 65
   # ASCII Value B is 66
    
    #..
    #..
    #..
   # ASCII Value Z is 89
    
Start =input("Enter the start of range : ")
End= input("Enter end of range : ")

for i in range(65,90):
    print("ASCII value of {} is {}".format((chr(i)),i))