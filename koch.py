from turtle import *
  
# function to create koch recursive_koch or koch curve
# size defines the size of the side
# level_number-level number
def recursive_koch(size, level_number):
    if level_number == 0:
        forward(size)
        return
    size /= 3.0
    recursive_koch(size, level_number-1)
    left(60)
    recursive_koch(size, level_number-1)
    right(120)
    recursive_koch(size, level_number-1)
    left(60)
    recursive_koch(size, level_number-1)
  
# main function
if __name__ == "__main__":
  
    # defining the speed of the turtle
    speed(0)                   
    size = 300.0              
  
    # Pull the pen up - no drawing when moving.
    penup()                     
      
    # Move the turtle backward by distance, 
    # opposite to the direction the turtle 
    # is headed.
    # Do not change the turtle's heading.
    backward(size/2.0)        
  
    # Pull the pen down - drawing when moving.
    pendown()         
    
    level_number =3

    recursive_koch(size, level_number)
  
    # To control the closing windows of the turtle
    mainloop() 