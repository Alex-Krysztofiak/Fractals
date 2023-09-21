from turtle import *
import turtle as t

def complement(s):
    comps = "";
 
    # finding the complement
    # of the string.
    for i in range(len(s)):
 
        # if character is 0, append 1
        if (s[i] == '0'):
            comps += '1';
 
        # if character is 1, append 0.
        else:
            comps += '0';
 
    return comps;
# Return the nth term of
# Thue-Morse sequence.
def nthTerm(n):
 
    # Initializing the string to 0
    s = "0";
 
    # Running the loop for n - 1 time.
    for i in range(1, n):
 
        # appending the complement of
        # the string to the string.
        s += complement(s);
     
    return s;
 


# Driver Code
array = []
n = 20;


# Turtle setting to make this look pretty
pen_color = int(100000)
t.hideturtle()
t.speed(speed=0)
t.pen(pencolor=f"#{pen_color}", pensize=1)
t.penup()
t.goto(-1100,600)
t.pendown()

# This is the code that runs the actual program

for char in nthTerm(n):
    array.append(char)
    
for i in range(len(array)):
    if array[i] == "1":
        fwd = 5
        turn = 0
        
    elif array[i] == "0":
        fwd = 0
        turn = 60
    t.right(turn)
    t.fd(fwd)
    pen_color += 11
    if pen_color > 999980:
        pen_color = 100000
    t.pen(pencolor=f"#{pen_color}")
    #This is going to check if the turtle is off screen, if it is, then we make the screen bigger?
    # print(pen_color)
    
t.mainloop()