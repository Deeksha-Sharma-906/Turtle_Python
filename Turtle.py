import numpy as np
from turtle import Turtle, Screen
import random
import math

t = Turtle()

screen = Screen()
screen.colormode(255)

t.shape("turtle")
t.width(5)

t.speed("fastest")

# t.clear()

#Draw dotted lines:
# t.shape("turtle")
# for _ in range(10):
#     t.forward(20)
#     t.penup()
#     t.forward(20)
#     t.pendown()

#Draw Dotted square
# for _ in range(4):
#     t.forward(40)
#     t.penup()
#     t.forward(40)
#     t.pendown()
#     t.forward(40)
#     t.right(90)

# #Draw a triangle:
# for i in range (3):
#     t.color('red')
#     t.forward(100)
#     t.right(120)
#
# #Draw a Square:
# for i in range(4):
#     t.color('blue')
#     t.forward(100)
#     t.right(90)
#
# #Draw a Pentagon:
# for i in range(5):
#     t.color('green')
#     t.forward(100)
#     t.right(72)
#
# #Draw a Hexagon:
# for i in range(6):
#     t.color('orange')
#     t.forward(100)
#     t.right(60)
#
# #Draw a Heptagon:
# for i in range(7):
#     t.color('purple')
#     t.forward(100)
#     t.right(51.43)
#
# #Draw a Octagon:
# for i in range(8):
#     t.color('yellow')
#     t.forward(100)
#     t.right(45)
#
# #Draw a Nonagon:
# for i in range(9):
#     t.color('pink')
#     t.forward(100)
#     t.right(40)
#
# #Draw a Decagon:
# for i in range(10):
#     t.color('black')
#     t.forward(100)
#     t.right(36)


#Draw shapes 3-10 with different colors:
# import random
# colors = ["red", "blue","green", "orange", "purple","yellow","pink","black"]
# for i in range(3,11):
#     angle = 360/i
#     t.color(random.choice(colors))
#     for _ in range(i):
#         t.forward(100)
#         t.right(angle)

#Draw a Star
# for i in range(5):
#     t.color('gold')
#     t.forward(150)
#     t.right(144)

#Draw Random Lines
# import random
#
# screen = Screen()
# screen.colormode(255)
# def random_colors():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r, g, b)
#     return random_color
#
# angle = [0, 90, 180, 270]
# t.speed(8)
# t.shape("arrow")
# t.width(10)
#
# for _ in range(150):
#     t.color(random_colors())
#     t.forward(30)
#     t.setheading(random.choice(angle))

#Draw a Spirograph
# import random
#
# screen = Screen()
# screen.colormode(255)
# def random_colors():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r, g, b)
#     return random_color
#
# angle = 5
# #nums = int(360/8)
#
# t.speed("fastest")
# for _ in range(int(360/angle)):
#     t.width(2)
#     t.color(random_colors())
#     t.circle(100)
#     t.right(angle)
#     #t.circle(100)


# MATH GRAPHS

#Sine Waves
# screen.title("Sine Wave")
# screen.setup(900, 500)
# screen.bgcolor("black")
# t.hideturtle()
# t.pensize(2)
# t.color("cyan")
#
# # params
# amplitude = 100
# frequency = 0.02
# step = 2
# start_x = -420
#
# t.penup()
# t.goto(start_x, 0)
# t.pendown()
#
# x = start_x
# while x <= 420:
#     y = amplitude * math.sin(frequency * (x - start_x))
#     t.goto(x, y)
#     x += step

#Lissajous Curve
# screen.title("Lissajous Curve")
# screen.setup(800, 600)
# screen.bgcolor("black")
# t.hideturtle()
# t.pensize(2)
# t.color("cyan")
#
# A = 200
# B = 200
# a = 3  # freq x
# b = 4  # freq y
# delta = math.pi / 2  # phase difference
#
# t.penup()
# t.goto(A * math.sin(0 + delta), B * math.sin(0))
# t.pendown()
#
# for i in range(0, 2000):
#     phase = i * 0.01
#     x = A * math.sin(a * phase + delta)
#     y = B * math.sin(b * phase)
#     t.pencolor((random.randint(50,255), random.randint(50,255), random.randint(50,255)))
#     t.goto(x, y)

#Wave Interference (two sine waves combined)

# screen.title("Wave Interference")
# screen.setup(900, 500)
# t.hideturtle()
# screen.bgcolor("black")
#
# # background grid-like axis
# axis = Turtle()
# axis.hideturtle()
# axis.speed(0)
# axis.color("gray")
# axis.penup()
# axis.goto(-420, 0); axis.pendown(); axis.goto(420, 0)
# axis.penup()
# axis.goto(0, -220); axis.pendown(); axis.goto(0, 220)
#
# t1 = Turtle(); t1.hideturtle(); t1.speed("fastest"); t1.pensize(2)
# t2 = Turtle(); t2.hideturtle(); t2.speed("fastest"); t2.pensize(2)
# t_sum = Turtle(); t_sum.hideturtle(); t_sum.speed("fastest"); t_sum.pensize(3)
#
# A1, A2 = 60, 40
# f1, f2 = 0.03, 0.05
# phase1, phase2 = 0, math.pi/4
# step = 2
# start_x = -420
#
# # draw two component waves
# t1.color(100, 200, 255); t1.penup(); t1.goto(start_x, 0); t1.pendown()
# t2.color(255, 100, 180); t2.penup(); t2.goto(start_x, 0); t2.pendown()
# t_sum.color("yellow"); t_sum.penup(); t_sum.goto(start_x, 0); t_sum.pendown()
#
# x = start_x
# while x <= 420:
#     rel_x = x - start_x
#     y1 = A1 * math.sin(2 * math.pi * f1 * rel_x + phase1)
#     y2 = A2 * math.sin(2 * math.pi * f2 * rel_x + phase2)
#     y_sum = y1 + y2
#     t1.goto(x, y1)
#     t2.goto(x, y2)
#     t_sum.goto(x, y_sum)
#     x += step


#FRACTALS

#Fractal Tree (recursive)

# screen.setup(800, 600)
# screen.title("Fractal Tree")
# screen.bgcolor("black")
#
# t.hideturtle()
# t.left(90)
# t.penup()
# t.goto(0, -250)
# t.pendown()
# t.pensize(2)
# t.color("lime")
#
# def fractal_branch(length, depth):
#     if depth == 0 or length < 5:
#         return
#     t.forward(length)
#     angle = random.uniform(15, 30)
#     shrink = random.uniform(0.6, 0.8)
#     t.right(angle)
#     fractal_branch(length * shrink, depth - 1)
#     t.left(angle * 2)
#     fractal_branch(length * shrink, depth - 1)
#     t.right(angle)
#     t.backward(length)
#
# fractal_branch(120, 7)

#Koch Snowflake
# screen.title("Koch Snowflake")
# screen.setup(800, 600)
# screen.bgcolor("black")
#
# t.hideturtle()
# t.speed("fastest")
# t.color("cyan")
# t.pensize(2)
#
# def koch(length, depth):
#     if depth == 0:
#         t.forward(length)
#     else:
#         koch(length/3, depth-1)
#         t.left(60)
#         koch(length/3, depth-1)
#         t.right(120)
#         koch(length/3, depth-1)
#         t.left(60)
#         koch(length/3, depth-1)
#
# t.penup()
# t.goto(-250, 100)
# t.pendown()
#
# for _ in range(3):
#     koch(500, 4)
#     t.right(120)

#Dragon Curve
# screen.title("Dragon Curve")
# screen.setup(800, 600)
# screen.bgcolor("black")
#
# t.hideturtle()
# t.speed("fastest")
# t.pensize(1)
# t.color("magenta")
# t.penup()
# t.goto(-200, 0)
# t.pendown()
#
# def dragon(sequence):
#     for move in sequence:
#         if move == "L":
#             t.left(90)
#         else:
#             t.right(90)
#         t.forward(5)
#
# # generate sequence
# seq = "L"
# for _ in range(12):  # depth 12 — adjustable
#     rev = seq[::-1]
#     rev = rev.replace("L", "X").replace("R", "L").replace("X", "R")
#     seq = seq + "L" + rev
#
# dragon(seq)


#Colorful Spiral
# def random_colors():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r, g, b)
#     return random_color
#
# t.speed("fastest")
# for i in range(200):
#     t.color(random_colors())
#     t.forward(i)
#     t.right(45)

#Flower Pattern

# for i in range(36):
#     t.color("orange")
#     t.circle(100)
#     t.right(10)

#Bar Graph
# data = [50, 120, 80, 150, 100]
# t.speed(5)
# for value in data:
#     t.begin_fill()
#     t.forward(value)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(value)
#     t.left(90)
#     t.forward(40)
#     t.left(90)
#     t.end_fill()

#Line Graph
#
# data = [20, 90, 60, 140, 80, 120]
# t.speed(3)
#
# t.penup()
# t.goto(-200, 0)
# t.pendown()
#
# for value in data:
#     t.goto(t.xcor() + 50, value)
#     print(t.xcor())

#Hypnotic Spiral
# screen.bgcolor("black")
# t.pencolor("cyan")
#
# size = 2
# for _ in range(400):
#     t.forward(size)
#     t.right(25)
#     size += 1

#Rotating Square
# screen.bgcolor("black")
# t.pencolor("yellow")
#
# angle = 10
#
# for i in range(int(360/angle)):
#     for _ in range(4):
#         t.forward(150)
#         t.right(90)
#     t.right(angle)

#Rainbow Spiral Walk
# screen.bgcolor("black")
#
# def random_colors():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r, g, b)
#     return random_color
#
# for i in range(200):
#     t.pencolor(random_colors())
#     t.forward(i * 2)
#     t.right(119)

#GAMES

#Snake Game (compact)
# import time
# screen.setup(600, 600)
# screen.bgcolor("black")
# screen.title("The Snake Game")
# screen.tracer(0)
#
# head = Turtle("square"); head.color("lime"); head.penup(); head.goto(0,0)
# segments = []
# delay = 0.07
# score = 0
#
# # food
# food = Turtle("circle"); food.color("red"); food.penup()
# food.goto(random.randint(-14,14)*20, random.randint(-14,14)*20)
#
# direction = "stop"
# def go_up():    global direction; direction = "up"
# def go_down():  global direction; direction = "down"
# def go_left():  global direction; direction = "left"
# def go_right(): global direction; direction = "right"
#
# screen.listen()
# screen.onkey(go_up, "w")
# screen.onkey(go_down, "s")
# screen.onkey(go_left, "a")
# screen.onkey(go_right, "d")
#
# def move():
#     x, y = head.xcor(), head.ycor()
#     if direction == "up": head.sety(y + 20)
#     if direction == "down": head.sety(y - 20)
#     if direction == "left": head.setx(x - 20)
#     if direction == "right": head.setx(x + 20)
#
# while True:
#     screen.update()
#     if direction != "stop":
#         move()
#     # collision with border
#     if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
#         time.sleep(1); head.goto(0,0); direction="stop"
#         for seg in segments: seg.goto(1000,1000)
#         segments.clear()
#     # eat food
#     if head.distance(food) < 20:
#         food.goto(random.randint(-14,14)*20, random.randint(-14,14)*20)
#         seg = Turtle("square"); seg.color("green"); seg.penup()
#         segments.append(seg)
#     # move tail
#     for i in range(len(segments)-1, 0, -1):
#         x = segments[i-1].xcor(); y = segments[i-1].ycor()
#         segments[i].goto(x, y)
#     if segments:
#         segments[0].goto(head.xcor(), head.ycor())
#
#     # self collision
#     for seg in segments:
#         if seg.distance(head) < 10:
#             time.sleep(1); head.goto(0,0); direction="stop"
#             for s in segments: s.goto(1000,1000)
#             segments.clear()
#
#     time.sleep(delay)


#Pong (classic)

# from turtle import Screen, Turtle
#
# screen = Screen()
# screen.setup(800, 600)
# screen.bgcolor("black")
# screen.title("Pong")
# screen.tracer(0)
#
# # paddles
# left_p = Turtle("square"); left_p.shapesize(stretch_wid=5, stretch_len=1); left_p.color("white"); left_p.penup(); left_p.goto(-350, 0)
# right_p = Turtle("square"); right_p.shapesize(stretch_wid=5, stretch_len=1); right_p.color("white"); right_p.penup(); right_p.goto(350, 0)
#
# ball = Turtle("circle"); ball.color("cyan"); ball.penup(); ball.dx = 4; ball.dy = 4
#
# def left_up(): left_p.sety(left_p.ycor() + 30)
# def left_down(): left_p.sety(left_p.ycor() - 30)
# def right_up(): right_p.sety(right_p.ycor() + 30)
# def right_down(): right_p.sety(right_p.ycor() - 30)
#
# screen.listen()
# screen.onkey(left_up, "w"); screen.onkey(left_down, "s")
# screen.onkey(right_up, "Up"); screen.onkey(right_down, "Down")
#
# while True:
#     screen.update()
#     ball.setx(ball.xcor() + ball.dx)
#     ball.sety(ball.ycor() + ball.dy)
#
#     if ball.ycor() > 290 or ball.ycor() < -290:
#         ball.dy *= -1
#     if ball.xcor() > 390:
#         ball.goto(0,0); ball.dx *= -1
#     if ball.xcor() < -390:
#         ball.goto(0,0); ball.dx *= -1
#
#     # paddle collision
#     if (ball.distance(right_p) < 50 and ball.xcor() > 320) or (ball.distance(left_p) < 50 and ball.xcor() < -320):
#         ball.dx *= -1

#Brick Breaker (compact)
# import random, time
# from turtle import Screen, Turtle
#
# screen = Screen()
# screen.setup(800, 600)
# screen.bgcolor("black")
# screen.title("Brick Breaker")
# screen.tracer(0)
#
# # paddle
# p = Turtle("square"); p.shapesize(1,5); p.color("white"); p.penup(); p.goto(0, -250)
# def paddle_left(): p.setx(p.xcor() - 40)
# def paddle_right(): p.setx(p.xcor() + 40)
# screen.listen(); screen.onkey(paddle_left, "Left"); screen.onkey(paddle_right, "Right")
#
# # ball
# ball = Turtle("circle"); ball.color("cyan"); ball.penup(); ball.goto(0, -220); ball.dx=4; ball.dy=4
#
# # bricks
# bricks = []
# colors = ["red","orange","yellow","green","purple"]
# start_x = -330
# start_y = 200
# for row in range(5):
#     y = start_y - row*30
#     for col in range(12):
#         b = Turtle("square"); b.shapesize(1,2); b.color(colors[row%len(colors)]); b.penup()
#         b.goto(start_x + col*60, y)
#         bricks.append(b)
#
# lives = 3
# score = 0
#
# while True:
#     screen.update()
#     ball.setx(ball.xcor() + ball.dx)
#     ball.sety(ball.ycor() + ball.dy)
#     # wall collisions
#     if ball.xcor() > 390 or ball.xcor() < -390:
#         ball.dx *= -1
#     if ball.ycor() > 290:
#         ball.dy *= -1
#     if ball.ycor() < -300:
#         lives -= 1
#         ball.goto(0,-220); ball.dy = 4; ball.dx = random.choice([4,-4])
#         if lives == 0:
#             break
#     # paddle collision
#     if ball.distance(p) < 50 and ball.ycor() < -230:
#         ball.dy *= -1
#     # brick collision
#     for b in bricks:
#         if b.distance(ball) < 30:
#             b.goto(1000,1000); bricks.remove(b)
#             ball.dy *= -1
#             score += 10
#     if not bricks:
#         break
#     time.sleep(0.01)

#Space Invasion — Nokia-style
import turtle, random, math
from turtle import Screen, Turtle

# ----- Screen -----
screen = Screen()
screen.setup(900, 600)
screen.title("Space Invasion")
screen.bgcolor("black")
screen.tracer(0)

# ----- HUD -----
score = 0
lives = 3

pen = Turtle(); pen.hideturtle(); pen.penup(); pen.color("white"); pen.goto(-420, 260)

def draw_hud():
    pen.clear()
    pen.goto(-420, 260)
    pen.write(f"Score: {score}", font=("Arial", 16, "normal"))
    pen.goto(220, 260)
    pen.write(f"Lives: {lives}", font=("Arial", 16, "normal"))

draw_hud()

# ----- Player -----
player = Turtle()
player.shape("triangle"); player.color("cyan")
player.penup(); player.setheading(0); player.goto(-380, 0)

PLAYER_SPEED = 30

def move_up():
    y = player.ycor() + PLAYER_SPEED
    if y > 260: y = 260
    player.sety(y)

def move_down():
    y = player.ycor() - PLAYER_SPEED
    if y < -260: y = -260
    player.sety(y)

screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")

# ----- Bullets (multiple) -----
bullets = []
BULLET_SPEED = 20

def fire():
    b = Turtle("circle")
    b.color("yellow"); b.shapesize(0.3, 0.3)
    b.penup()
    b.goto(player.xcor() + 20, player.ycor())
    bullets.append(b)

screen.onkey(fire, "space")

# ----- Enemies -----
enemies = []
ENEMY_SPEED_MIN = 2
ENEMY_SPEED_MAX = 5

def spawn_enemy():
    e = Turtle()
    shape = random.choice(["circle", "square", "triangle"])
    e.shape(shape)
    size = random.choice([0.8, 1.2, 1.6])
    e.shapesize(size)
    e.color(random.choice(["red","orange","magenta","white"]))
    e.penup()
    x = 480
    y = random.randint(-260, 260)
    e.goto(x, y)
    e.speed = random.uniform(ENEMY_SPEED_MIN, ENEMY_SPEED_MAX)
    enemies.append(e)

# spawn initial wave
for _ in range(6):
    spawn_enemy()

# ----- Power-ups (extra life) -----
powerups = []
def spawn_powerup():
    p = Turtle("circle")
    p.color("green"); p.shapesize(1.2)
    p.penup()
    p.goto(480, random.randint(-220,220))
    p.speed = 2
    powerups.append(p)

# ----- Collision util -----
def collided(a, b, threshold=20):
    return a.distance(b) < threshold

# ----- Restart button -----
def restart_game(x=None, y=None):
    global score, lives, enemies, bullets, powerups
    score = 0; lives = 3
    # clear enemies/bullets/powerups
    for e in enemies: e.goto(1000,1000)
    for b in bullets: b.goto(1000,1000)
    for p in powerups: p.goto(1000,1000)
    enemies = []; bullets = []; powerups = []
    for _ in range(6): spawn_enemy()
    draw_hud()
    screen.update()
    game_loop()

restart_btn = Turtle()
restart_btn.hideturtle(); restart_btn.color("white"); restart_btn.penup()
restart_btn.goto(0, -280)
restart_btn.write("Click here to Restart", align="center", font=("Arial", 14, "normal"))
restart_btn.goto(0, -300)
screen.onclick(lambda x, y: restart_game(x,y))  # click anywhere to restart

# ----- Main loop -----
game_over = False
spawn_timer = 0
powerup_timer = 0

def game_loop():
    global score, lives, game_over, spawn_timer, powerup_timer

    if game_over:
        return

    # spawn enemies periodically
    spawn_timer += 1
    if spawn_timer > 60:
        spawn_timer = 0
        spawn_enemy()

    # spawn powerups occasionally
    powerup_timer += 1
    if powerup_timer > 400:
        powerup_timer = 0
        spawn_powerup()

    # move enemies left
    for e in enemies:
        e.setx(e.xcor() - e.speed)
        # if reaches left edge -> player hit
        if e.xcor() < -420:
            e.goto(1000,1000); enemies.remove(e)
            lives -= 1
            draw_hud()
            if lives <= 0:
                end_game("GAME OVER")
                return

    # move bullets
    for b in bullets:
        b.setx(b.xcor() + BULLET_SPEED)
        if b.xcor() > 480:
            b.goto(1000, 1000)
            if b in bullets: bullets.remove(b)

    # move powerups
    for p in list(powerups):
        p.setx(p.xcor() - p.speed)
        if p.xcor() < -480:
            p.goto(1000,1000); powerups.remove(p)

    # collisions: bullets vs enemies
    for b in list(bullets):
        for e in list(enemies):
            if collided(b, e, threshold=20):
                # destroy enemy and bullet
                e.hideturtle(); e.goto(1000,1000); enemies.remove(e)
                b.hideturtle(); b.goto(1000,1000); bullets.remove(b)
                score += 10
                draw_hud()
                break

    # collisions: player vs enemies
    for e in list(enemies):
        if collided(player, e, threshold=20):
            e.hideturtle(); e.goto(1000,1000); enemies.remove(e)
            lives -= 1
            draw_hud()
            if lives <= 0:
                end_game("YOU WERE HIT!")
                return

    # collisions: player vs powerups
    for p in list(powerups):
        if collided(player, p, threshold=20):
            p.hideturtle(); p.goto(1000,1000); powerups.remove(p)
            lives += 1
            draw_hud()

    screen.update()
    screen.ontimer(game_loop, 16)

def end_game(msg):
    global game_over
    game_over = True
    g = Turtle(); g.hideturtle(); g.color("white"); g.penup(); g.goto(0,0)
    g.write(msg, align="center", font=("Arial", 32, "bold"))
    g.goto(0, -40)
    g.write(f"Final Score: {score}", align="center", font=("Arial", 18, "normal"))
    # show restart instruction
    restart_btn.clear()
    restart_btn.goto(0, -80)
    restart_btn.write("Click anywhere to Restart", align="center", font=("Arial", 14, "normal"))

# start game
draw_hud()
game_loop()
screen.mainloop()



screen = Screen()
screen.exitonclick()
