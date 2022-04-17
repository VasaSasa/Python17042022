
#task 1
#square_side = int(input("Enter square's side: "))

#symbol = "*"


#for i in range(square_side):
    #print(square_side*symbol)


#task 1 again

#square_side = int(input("Enter square's side: "))
#symbol = "*"
#one_side = symbol * square_side


#print((one_side + "\n") * square_side)


#print("Hello",end="")
#print(" Dave")
#print("Dave","Ema","John",sep="222")

#task 1 again Petr Sedláček


#square_side = int(input("Enter square's side: "))
#symbol = "*"

#for i in range(square_side):
    #for j in range(square_side):
        #print(symbol, end="")
    #print("a")


#TASK 2

#The user types in the width and height of a rectangle. Print
#a solid rectangle of the specified height and width. Say the user
#typed in the height equal to 3, and width 5, the output should
#be as follows:
#*****
#*****
#*****


#width = int(input("Enter the width of rectangle: "))
#height = int(input("Enter the height of rectangle: "))
#symbol = "*"

#x = 0
#while x < width:
    #y = 0
    #print(x * symbol)
    #while y < height:
        #print(y * symbol)
        #y += 1
    #x += 1

#for i in range(height):
    #print(symbol * width)

#TASK 3

#The user types in the size of the square’s sides. Print an empty
#square (only its sides are displayed). The side is equal to the
#typed in size.



#square_side = int(input("Enter square's side: "))
#symbol = "*"


#first_row = symbol * square_side
#print(first_row)

#for i in range(square_side -2):
    #print(symbol," " * (square_side - 4), symbol)  # místo "-4" bych čekal, že tam půjde -2#

#last_row = symbol * square_side
#print(last_row)


#TASK 3 Petr Sedláček

#square_side = int(input("Enter square's side: "))
#symbol = "*"


#for i in range(square_side):
    #for j in range(square_side):
        #if i == 0 or j == 0 or i == square_side - 1 or j == square_side -1:
            #print(symbol,end="")
        #else:
            #print(" ",end="")
    #print()




#TASK 4
#The user types in the length and width of a rectangle. Print
#an empty rectangle (only its sides are displayed). The length
#and width are equal to the typed in numbers.

width_rectangle = int(input("Enter width of rectangle: "))
height_rectangle = int(input("Enter height of rectangle: "))
symbol = "*"

for i in range(height_rectangle): # rows
    for j in range(width_rectangle): # column10
        if i == 0 or j == 0 or i == height_rectangle - 1 or j == width_rectangle - 1:
            print(symbol, end="")
        else:
            print(" ", end="")
    print()









#my TASKs

#print(("Vašek" + "\n") * 5)

#range001 = 10
#for i in range(range001):
    #print("Vašek ",end="")


#print("Vašek","Vašek", "Vašek",sep="  222  ")


