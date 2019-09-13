#!/usr/bin/env python2
#encoding=utf-8

import  turtle  as tt
import  math
import  time

tt.hideturtle()
tt.speed(10)

def draw_circle(r):
    tt.penup()
    tt.goto(0, -r)
    tt.seth(0)
    tt.pendown()
    tt.pensize(5)
    tt.color('#F8CD32','#FBA92D')
    tt.begin_fill()
    tt.circle(r)
    tt.end_fill()

def draw_petal(r, n):
    tt.penup()
    tt.goto(0, -r)
    tt.seth(0)
    tt.pendown()

    small_r = math.sin( math.pi/n) * r
    
    for i in range(n):
        tt.penup()
        tt.home()
        tt.seth((360/n)*i)
        tt.fd(r)
        tt.left((360/n)*0.5)
        tt.pendown()
        tt.color('#F0BE7C')
        tt.begin_fill()
        tt.circle(small_r,180)
        tt.end_fill()

def draw_square(d, r):
    tt.penup()
    tt.seth(0)
    tt.goto(d/2 + r, -d/2)
    tt.left(90)
    tt.pendown()
    
    for i in range(4):
        tt.fd(d)
        tt.circle(r, 90)

def draw_word(word, x, y):
    tt.penup()
    tt.goto(x, y)
    tt.pendown()
    tt.color("Gold")
    tt.write(word, font=("微软雅黑",35, "normal"))



def draw():
    tt.title("FlyPython祝您中秋快乐")
    draw_circle(120)
    draw_petal(120,18)
    #draw_square(100,10)
    draw_word("五",-50,5)
    draw_word("最",0,5)
    draw_word("仁",-50,-40)
    draw_word("棒",0,-40)
    tt.done()


if __name__ == "__main__":
    time.sleep(10)
    draw()

