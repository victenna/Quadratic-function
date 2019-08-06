import turtle,time
import grid_module1
#from grid_module1 import GRIDS
wn=turtle.Screen()
wn.setup(950,900)
wn.tracer(10)
t1=turtle.Turtle()
t1.setheading(0)
t1.pensize(5)
t1.hideturtle()
t1.up()
r=-1
clr=['blue','red','green']
while True:
    def shift(a,h,k):
        #global X,Y
        #A=40/Q
        X1=-400
        Y1=a*(X1-h)*(X1-h)+k
        t1.up()
        t1.setposition(X1,Y1)
        deltax=2
        
        for q in range(0,400):
            X=(X1+q*deltax)
            Y=a/25*(X-25*h)*(X-25*h)+25*k
            if abs(Y)<370 and abs(X)<360:
                
                #print(Y)
                t1.down()
            else:
                t1.up()
            t1.setposition(X,Y)
    r=r+1
    r1=r%3
    a1=float(wn.textinput('Quadratic Function','Enter value a'))
    h1=float(wn.textinput('Quadratic Function','Enter value h'))
    k1=float(wn.textinput('Quadratic Function','Enter value k'))
    print(k1)
    t1.color(clr[r1])
    shift(a1,h1,k1)
    if r1==2:
        time.sleep(4)
        t1.clear()

