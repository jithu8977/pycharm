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



print(draw_rectangle(width,height))
turtle.mainloop()