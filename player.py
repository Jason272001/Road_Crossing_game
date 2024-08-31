from turtle import Turtle



class Player(Turtle):
     def __init__(self):
         super().__init__()
         self.create_player()


     def create_player(self):
         self.shape("turtle")
         self.color("white")
         self.shapesize(stretch_wid=1.25,stretch_len=1.25)
         self.left(90)
         self.penup()
         self.goto_start()

     def up(self):
         new_Y=self.ycor()+25
         self.goto(self.xcor(),new_Y)

     def down(self):
         if self.ycor()>-350:
             new_Y=self.ycor()-25
             self.goto(self.xcor(),new_Y)

     def left_move(self):
         if self.xcor() > -350:
             new_X = self.xcor() - 25
             self.goto(new_X,self.ycor())

     def right(self):
         if self.xcor() < 350:
             new_X = self.xcor() + 25
             self.goto(new_X,self.ycor())

     def finish_line(self):
         if self.ycor()>350:
             return True
         else:
             return False
     def goto_start(self):
         self.goto(0,-350)