import turtle

def goto(john, x, y):
    john.up()
    john.goto(x, y)
    john.setheading(0)
    john.down()

def drawCircle(john, radius, drawColor, fillColor, isFillEnable):
    john.color(drawColor)
    john.fillcolor(fillColor)

    if isFillEnable:
        john.begin_fill()

    john.circle(radius)

    if isFillEnable:
        john.end_fill()

def drawTriangle(john, sideSize, drawColor, fillColor, isFillEnable):
    john.color(drawColor)
    john.fillcolor(fillColor)

    if isFillEnable:
        john.begin_fill()

    john.forward(sideSize)
    john.right(240)
    john.forward(sideSize)
    john.right(240)
    john.forward(sideSize)

    if isFillEnable:
        john.end_fill()

def drawRectangle(john, sideSizeL, sideSizel, drawColor, fillColor, isFillEnable):
    john.color(drawColor)
    john.fillcolor(fillColor)

    if isFillEnable:
        john.begin_fill()

    john.forward(sideSizeL)
    john.right(270)
    john.forward(sideSizel)
    john.right(270)
    john.forward(sideSizeL)
    john.right(270)
    john.forward(sideSizel)

    if isFillEnable:
        john.end_fill()

def title(drawArea, fontSize):
    john = turtle.RawTurtle(drawArea)
    john.hideturtle()
    john.speed(0)

    john.up()
    john.goto(-170, 100)
    john.write("Title : ", font=("Arial", 10, "bold"))
    john.goto(-150, 0)
    john.down()

    john.write("Merry christmas ! ", font=("Segoe script", fontSize, "bold"))

def snowStar(drawArea, scale):
    colorList = ["cyan", "dark blue"]
    john = turtle.RawTurtle(drawArea)
    john.hideturtle()
    john.speed(0)

    john.up()
    john.goto(-170, 100)
    john.write("Snow star : ", font=("Arial", 10, "bold"))
    john.goto(0, 0)
    john.down()

    for x in range(9):
        john.fillcolor(colorList[x%2])
        john.begin_fill()
        for x in range(2):
            john.forward(100 * scale)
            john.right(60)
            john.forward(100 * scale)
            john.right(120)
        john.end_fill()
        john.right(36)

    john.fillcolor(colorList[1])
    john.begin_fill()
    john.forward(100 * scale)
    john.right(60)
    john.forward(100 * scale)
    john.right(120)
    john.forward(72 * scale)
    john.right(96)
    john.forward(28 * scale)
    john.left(60)
    john.forward(100 * scale)
    john.end_fill()

def fractalChristmasTree(drawArea, scale):
    john = turtle.RawTurtle(drawArea)
    john.hideturtle()
    john.speed(0)

    john.up()
    john.goto(-170, 100)
    john.write("Fractal Christmas tree : ", font=("Arial", 10, "bold"))
    john.goto(0, 0)
    john.down()

    john.left(90)
    john.color("dark green")
    john.backward(scale * 2)

    def branch(d, s):
        if d <= 0: return
        john.forward(s)
        branch(d - 1, s * .8)
        john.right(120)
        branch(d - 3, s * .5)
        john.right(120)
        branch(d - 3, s * .5)
        john.right(120)
        john.backward(s)

    branch(15, scale)

def snowMan(drawArea, startPosX, startPosY, scale):
    john = turtle.RawTurtle(drawArea)
    john.hideturtle()
    john.speed(0)

    john.up()
    john.goto(-170, 100)
    john.write("Snow Man : ", font=("Arial", 10, "bold"))
    john.goto(0, 0)
    john.down()

    #body
    goto(john, 0, -80)
    drawCircle(john, 50, "white", "white", True)
    goto(john, 0, 0)
    drawCircle(john, 30, "white", "white", True)
    goto(john, 0, 50)
    drawCircle(john, 20, "white", "white", True)

    #eyes
    goto(john, -7, 70)
    drawCircle(john, 3, "black", "black", True)
    goto(john, 7, 70)
    drawCircle(john, 3, "black", "black", True)

    #mouth
    goto(john, 0, 50)
    drawCircle(john, 7, "black", "black", True)
    goto(john, 0, 54)
    drawCircle(john, 6, "white", "white", True)

    #noze
    goto(john, 0, 60)
    drawCircle(john, 2, "orange", "orange", True)

    #hat
    goto(john, -20, 90)
    drawTriangle(john, 40, "red", "red", True)
    goto(john, -20, 86)
    drawCircle(john, 7, "white", "white", True)
    goto(john, -10, 86)
    drawCircle(john, 7, "white", "white", True)
    goto(john, 0, 86)
    drawCircle(john, 7, "white", "white", True)
    goto(john, 10, 86)
    drawCircle(john, 7, "white", "white", True)
    goto(john, 20, 86)
    drawCircle(john, 7, "white", "white", True)
    goto(john, 0, 125)
    drawCircle(john, 7, "white", "white", True)

    #arms
    goto(john, 25, 35)
    john.setheading(25)
    drawRectangle(john, 50, 7, "brown", "brown", True)
    goto(john, -25, 40)
    john.setheading(150)
    drawRectangle(john, 50, 7, "brown", "brown", True)

    #buttons
    goto(john, 0, 0)
    drawCircle(john, 2, "black", "black", True)
    goto(john, 0, -10)
    drawCircle(john, 2, "black", "black", True)
    goto(john, 0, -20)
    drawCircle(john, 2, "black", "black", True)
    goto(john, 0, -30)
    drawCircle(john, 2, "black", "black", True)
    goto(john, 0, -40)
    drawCircle(john, 2, "black", "black", True)
    goto(john, 0, -50)
    drawCircle(john, 2, "black", "black", True)

def starStyle2(drawArea, scale):
    colors = ['orange', 'yellow']
    john = turtle.RawTurtle(drawArea)
    john.hideturtle()
    john.speed(0)

    john.up()
    john.goto(-170, 100)
    john.write("Star : ", font=("Arial", 10, "bold"))
    john.goto(0, 0)
    john.down()

    for x in range(200):
        john.pencolor(colors[x%2])
        john.width((x//100 + 1) * scale)
        john.forward(x * scale)
        john.left(59)