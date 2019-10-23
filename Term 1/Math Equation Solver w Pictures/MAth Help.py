#Taya Martinez, Kaydon Payne, Jessica Adams, Isaac Lehman
#Testers: Bales, Greyson, Ian Christensen, Jayden Williams,Max Virkus
#9/11/19
#Geometry Homework Helper

# If in a program and click enter, shuts program

#Perm of sqr
## If there is a float it breaks and exits program instantly
## If the number is to big, the square gets pushed out
## If you put letters it exits program

#Area of sqr
## Letters break it
## floats break it
## if number is to big or to small square gets skewed
## special charecters break

#Circumference of a circle
## Letters break
## Big numbers skew
## Shows to many decimal places
## Special charecters break

#area of a triangle
## The number for height is shown on the diagonal of the hypot.
## Letters break

#Volume of a cube
## Skewed with a small number
## float dont work
## strings exit program




#I added in ascii art since I may or may not be in class because of a funeral...-Kaydon Payne

while True:

  print("""
             _            _       _             
    ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
   / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
  | (_| (_| | | (__| |_| | | (_| | || (_) | |   
   \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

  """)
  print("""What problem are you trying to solve?")
  Perimeter of a square = 1")
  Area of a square = 2")
  Circumference of a circle = 3")
  Area of a triangle = 4")
  Volume of a cube = 5")
  Area of a triangle = 6
  To leave type 'end'""")
  choice=input("Type the corresponding number: ")

  if choice=="1":
    #Perimeter of a square
    print("""
               _            _       _             
      ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
     / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
    | (_| (_| | | (__| |_| | | (_| | || (_) | |   
     \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

    """)
    print("Finding Perimeter of a Square")
    side_length = input("What is the side length of the square?")
    perimeter = int(side_length)*4
    perimeter = str(perimeter)+"ft"
    square1 = str.format("""  
         _______
        |       |
        |       |{0}ft
        | {1:^6}|
        |_______|
         
    Side Length: {0}ft
    Perimeter: {1}
    """,side_length,perimeter)
    print(square1)
    input()
  elif choice=="2":
    #Area of a square

    print("""
               _            _       _             
      ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
     / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
    | (_| (_| | | (__| |_| | | (_| | || (_) | |   
     \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

    """)
    print("Finding The Area of a Square")
    side_length = input("What is the side length of the square?")
    area = int(side_length)*int(side_length)
    area = str(area)+"ft^2"
    square = str.format("""
      
       _______
      |       |
      |       |{0}ft
      | {1:^5}|
      |_______|
          

    Side Length: {0}ft
    Area:{1}
    """,side_length,area)
    print(square)
    input()

  elif choice=="3":
    #Circumference of a circle
    print("""
               _            _       _             
      ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
     / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
    | (_| (_| | | (__| |_| | | (_| | || (_) | |   
     \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

    """)
    pi=3.14159265
    print("""Circumference of a circle = 2πR""")
    rad=input("Radius: ")
    cir=float(2)*float(pi)*float(rad)
    cir_Final=str.format("{0:.2f}",cir)
    cir_Final=cir_Final+"ft"
    circle = str.format("""
                     
                 _____
              .-'     '-.
            .'           '.
           /               \\
          ;    {0:^5}        ;
          |---------        |{1}ft
          ;                 ;
           \\               /
            '.           .'
              '-._____.-'
                  

    Radius: {1}ft
    Circumference: {0}ft
    """,rad,cir_Final)
    print(circle)
    input()
  elif choice=="4":
    #-AREA OF TRIANGLE-
    #variables for base and height--(triHeight is height, triBase is base)
    print("""
               _            _       _             
      ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
     / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
    | (_| (_| | | (__| |_| | | (_| | || (_) | |   
     \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

    """)
    print("finding the Area of Triangles")
    triHeight=input("enter triangle's height: ")
    triBase=input("enter triangle's base length: ")
      #triArea is area of triangle--(base*height/2)
    triArea= float(triHeight)*float(triBase)
    triArea=float(triArea)/2
    triArea=str(triArea)+"sqft"
      #printing solution
    triangle = str.format("""
            
                _____
               /    /\\
              /    /  \\
             /    /    \\
            /    /  /\\  \\
           /    /  /  \\  \\   {0}ft
          /    /  /\\   \\  \\
         /    /  /  \\   \\  \\
        /    /__/____\\   \\  \\
       /{1:^14}\\   \\  \\
      /________________\\   \\  \\
      \_____________________\\_ /
                  {2}ft
                   
    HeightHeight: {0}ft
    AreaArea: {1}ft
    BaseBase: {2}sqft
    """,triHeight,triArea,triBase)
    print(triangle)
    input()



  elif choice=="5":
    #Volume Of A Cube
    print("""
               _            _       _             
      ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
     / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
    | (_| (_| | | (__| |_| | | (_| | || (_) | |   
     \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

    """)
    print("Volume of a Cube")
    a = input ("what is the length of any one side: ")
    volume = float(a)*float(a)*float(a)
    cube = str.format("""



    @ + + + + + + + + + + + @
    +\\                      +\\
    + \\                     + \\
    +  \\                    +  \\{0}ft
    +   \\                   +   \\
    +    @ + + + + + + + + +++ + @
    +    +                  +    +
    +    +                  +    +
    +    +                  +    +
    +    +     {1:^3.2e}     +    + {0}ft
    +    +                  +    +
    +    +                  +    +
    @ + +++ + + + + + + + + @    +
     \\   +                   \\   +
      \\  +                    \\  +
       \\ +                     \\ +
        \\+                      \\+
         @ + + + + + + + + + + + @
                      {0}ft

    Length: {0}ft
    Width: {0}ft
    Height: {0}ft
    Volume: {1}ft^3
    """,a,volume)

    print(cube)
    input()
    
   #TRIANGLE AREA:

  elif choice=="6":
    #variables for base and height--(triHeight is height, triBase is base)
    triHeight=float(input("enter triangle's height: "))
    triBase=float(input("enter triangle's base: "))

    #triArea is area of triangle--(base*height/2)
    triArea= float(triHeight)*float(triBase)/2


    print(str.format("""\


                |        | 
               /|\\       | 
              / | \\      | 
             /  |  \\   {0:.2f}
            /   |   \\    | 
           /    |    \\   | 
          ------|------  |
             {1:.2f} 
        Area= {2:.2f}" un. squared """,triHeight,triBase,triArea))


    input()
  elif choice=="end":
    print("GoodBye!")
    exit()

      #It's perfect! Great job team! You all slayed it with this project, we got it done, and it looks suteki!

