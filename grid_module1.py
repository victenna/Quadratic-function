import turtle
wn=turtle.Screen()
wn.setup(900,900)
wn.bgcolor('gold')
turtle.tracer(2)
t2=turtle.Turtle()
t2.hideturtle()
t2.up()
Text_font=('Arial',20,'bold')
Text_font1=('Arial',10,'bold')
t2.goto(-450,400)
t2.color('blue')
t2.write('Quadratic Function in Vertex Form', font=Text_font)
t2.up()
image='function.gif'
wn.addshape(image)
t2.shape(image)
t2.goto(200,410)
t2.showturtle()
def GRIDS():
    tgrid=turtle.Turtle('triangle')
    tgrid.up()
    tgrid.hideturtle()
    tgrid.speed(0)
    tgrid.pensize(1)
    box=25
    A=15
    B=16
    def grid(dir,a,b,c,d):
         
         for j in range (-A,B):
              tgrid.setheading(dir)
              tgrid.penup()
              tgrid.goto(a*box*j-A*box*b,-box*A*c+box*j*d)
              tgrid.pendown()
              if j==0:
                   tgrid.pensize(3)
                   tgrid.fd(2*box*(A+0.5))
                   tgrid.stamp()
                   tgrid.fd(-2*box*(A+0.5))
              tgrid.pensize(1)
              tgrid.fd(2*box*A)
    grid(90,1,0,1,0)
    grid(0,0,1,0,1)

    txy=turtle.Turtle()
    txy.hideturtle()
    txy.goto(-A*box,0)

    def numbers(axis):
        for i in range (-A,B):
            txy.write(i)
            txy.fd(box)
            if i==A:
                txy.write(axis,font=('Arial',30,'bold'))
    numbers('X')
    txy.penup()
    txy.goto(5,-A*box)
    txy.setheading(90)
    numbers('Y')
GRIDS()
