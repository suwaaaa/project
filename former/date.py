import time
import turtle as t


def drawline(draw):
    t.pendown() if draw else t.penup()
    t.fd(40)
    t.right(90)


def drawdigit(digit):
    drawline(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 6, 8, ] else drawline(False)
    t.left(90)
    drawline(True) if digit in [0, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 1, 2, 3, 4, 5, 7, 8, 9] else drawline(False)
    t.left(180)
    t.penup()
    t.fd(40)


def gavetime(date):
    for i in date:
        if i == '-':
            t.write('年', font=("Arial", 30, "normal"))
            t.pencolor("green")
            t.fd(80)
        elif i == '+':
            t.write('月', font=("Arial", 30, "normal"))
            t.pencolor("purple")
            t.fd(80)
        elif i == '/':
            t.write('日', font=("Arial", 30, "normal"))
            t.pencolor("pink")
            t.fd(80)
        else:
            drawdigit(eval(i))


def main():
    t.setup(1000, 350, 200, 200)
    t.penup()
    t.fd(-400)
    t.pensize(5)
    gavetime(time.strftime('%Y-%m+%d/', time.gmtime()))
    t.hideturtle()
    t.done()


main()
