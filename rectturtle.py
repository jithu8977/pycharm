import turtle

width = float(input("Enter width"))
height = float(input("Enter height"))
def draw_rectangle(width, height):

  bob=turtle.Turtle()

  bob.fd(width)
  bob.lt(90)
  bob.fd(height)
  bob.lt(90)
  bob.fd(width)
  bob.lt(90)
  bob.fd(height)
  bob.lt(90)


bob1=turtle.Turtle()
def polygon_circle(bob1,n,length):

  for i in range(n):
    bob1.left(360/n)
    bob1.forward(length)
def draw_circle(bob1,r):
  circumfurence=2*(22/7)*r
  n=50
  length=circumfurence/n
  polygon_circle(bob1,n,length)

#bob1.exitonclick()
print(draw_circle(bob1,100))

print(draw_rectangle(width,height))
turtle.mainloop()