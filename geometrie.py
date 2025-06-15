import turtle
ninja=turtle.Turtle()
ninja.penup()
ninja.shape("turtle")
ninja.color("red")

def quadrat(seite,farbe,x,y):
  ninja.color(farbe)
  ninja.setx(x)
  ninja.sety(y)
  ninja.pendown()
  for i in range(4):
    ninja.forward(seite)
    ninja.left(90)
  ninja.penup()
def dreieck(seite,farbe,x,y):   
  ninja.color(farbe)
  ninja.setx(x)
  ninja.sety(y)
  ninja.pendown()    
  for i in range(3):
    ninja.forward(seite)
    ninja.left(120)
  ninja.penup()