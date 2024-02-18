import turtle
import random
t1 = turtle
t1.speed(0)
t1.bgcolor('black')

colors = ['red', 'blue', 'yellow', 'green']
n = 2000

for i in range(1, n+1):
    t1.pencolor(colors[int(random.randrange(0,4))])
    t1.rt(135)
    t1.fd(i/4)


t1.done()