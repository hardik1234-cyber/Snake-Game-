import turtle
import time
import random

class SnakeGame:
    def __init__(self):
        # Screen setup
        self.wn = turtle.Screen()
        self.wn.title("Snake Game by Walter007")
        self.wn.bgcolor("green")
        self.wn.setup(width=600, height=600)
        self.wn.tracer(0)

        # Game attributes
        self.delay = 0.1
        self.score = 0
        self.high_score = 0

        # Snake head
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("black")
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = 'stop'

        # Food
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.food.goto(0, 100)

        # Segments
        self.segments = []

        # Score display
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

    def update_score(self):
        """Update the score display."""
        self.pen.clear()
        self.pen.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def move(self):
        """Move the snake in the current direction."""
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)
        elif self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)
        elif self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)
        elif self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)

    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    def check_collision_with_food(self):
        """Check for collision with food and update segments and score."""
        if self.head.distance(self.food) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            self.food.goto(x, y)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            self.segments.append(new_segment)

            self.score += 10
            if self.score > self.high_score:
                self.high_score = self.score

            self.update_score()

    def check_collisions_with_wall_and_self(self):
        """Check for collision with wall and self, reset game if collided."""
        if abs(self.head.xcor()) > 290 or abs(self.head.ycor()) > 290:
            self.reset_game()

        for segment in self.segments:
            if segment.distance(self.head) < 20:
                self.reset_game()

    def reset_game(self):
        """Reset the game when collision occurs."""
        time.sleep(1)
        self.head.goto(0, 0)
        self.head.direction = "stop"

        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()

        self.score = 0
        self.update_score()

        self.delay = 0.1

    def move_segments(self):
        """Move each segment to follow the segment in front of it."""
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)

        if len(self.segments) > 0:
            x = self.head.xcor()
            y = self.head.ycor()
            self.segments[0].goto(x, y)

    def run(self):
        """Main game loop."""
        self.wn.listen()
        self.wn.onkey(self.go_up, "w")
        self.wn.onkey(self.go_down, "s")
        self.wn.onkey(self.go_left, "a")
        self.wn.onkey(self.go_right, "d")

        while True:
            self.wn.update()

            self.check_collision_with_food()
            self.check_collisions_with_wall_and_self()

            self.move_segments()
            self.move()

            time.sleep(self.delay)

# Instantiate and run the game
game = SnakeGame()
game.run()
