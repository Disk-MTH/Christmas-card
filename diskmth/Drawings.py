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

def drawStar(john, sideSize, drawColor, fillColor, isFillEnable):
    john.color(drawColor)
    john.fillcolor(fillColor)

    if isFillEnable:
        john.begin_fill()

    john.forward(sideSize)
    john.right(144)
    john.forward(sideSize)
    john.right(144)
    john.forward(sideSize)
    john.right(144)
    john.forward(sideSize)
    john.right(144)
    john.forward(sideSize)

    if isFillEnable:
        john.end_fill()


def title(drawArea, startPosX, startPosY, fontSize):
    john = turtle.RawTurtle(drawArea)
    john.hideturtle()
    john.speed(0)

    goto(john, startPosX, startPosY)

    john.write("Merry christmas ! ", font=("Segoe script", fontSize, "bold"))

def snowStar(drawArea, startPosX, startPosY, scale):
    colorList = ["cyan", "dark blue"]
    john = turtle.RawTurtle(drawArea)
    john.hideturtle()
    john.speed(0)

    goto(john, startPosX, startPosY)

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

def fractalChristmasTree(drawArea, startPosX, startPosY, scale):
    john = turtle.RawTurtle(drawArea)
    john.hideturtle()
    john.speed(0)

    goto(john, startPosX, startPosY)

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

def startStyle1(drawArea, startPosX, startPosY, scale):
    john = turtle.RawTurtle(drawArea)
    john.hideturtle()
    john.speed(0)

    goto(john, startPosX + 0 * scale, startPosY + 0 * scale)
    drawStar(john, 100 * scale, "yellow", "yellow", True)
    goto(john, startPosX + 10 * scale, startPosY - 3 * scale)
    drawStar(john, 80 * scale, "red", "red", True)
    goto(john, startPosX + 20 * scale, startPosY - 6 * scale)
    drawStar(john, 60 * scale, "yellow", "yellow", True)

def starStyle2(drawArea, startPosX, startPosY, scale):
    colors = ['orange', 'yellow']
    john = turtle.RawTurtle(drawArea)
    john.hideturtle()
    john.speed(0)

    goto(john, startPosX, startPosY)

    for x in range(200):
        john.pencolor(colors[x%2])
        john.width((x//100 + 1) * scale)
        john.forward(x * scale)
        john.left(59)

def snowMan(drawArea, startPosX, startPosY, scale):
    john = turtle.RawTurtle(drawArea)
    john.hideturtle()
    john.speed(0)

    #body
    goto(john, startPosX + 0 * scale, startPosY - 80 * scale)
    drawCircle(john, 50 * scale, "white", "white", True)
    goto(john, startPosX + 0 * scale, startPosY + 0 * scale)
    drawCircle(john, 30 * scale, "white", "white", True)
    goto(john, startPosX + 0 * scale, startPosY + 50 * scale)
    drawCircle(john, 20 * scale, "white", "white", True)

    #eyes
    goto(john, startPosX - 7 * scale, startPosY + 70 * scale)
    drawCircle(john, 3 * scale, "black", "black", True)
    goto(john, startPosX + 7 * scale, startPosY + 70 * scale)
    drawCircle(john, 3 * scale, "black", "black", True)

    #mouth
    goto(john, startPosX + 0 * scale, startPosY + 50 * scale)
    drawCircle(john, 7 * scale, "black", "black", True)
    goto(john, startPosX + 0 * scale, startPosY + 54 * scale)
    drawCircle(john, 6 * scale, "white", "white", True)

    #noze
    goto(john, startPosX + 0 * scale, startPosY + 60 * scale)
    drawCircle(john, 2 * scale, "orange", "orange", True)

    #hat
    goto(john, startPosX - 20 * scale, startPosY + 90 * scale)
    drawTriangle(john, 40 * scale, "red", "red", True)
    goto(john, startPosX - 20 * scale, startPosY + 86 * scale)
    drawCircle(john, 7 * scale, "white", "white", True)
    goto(john, startPosX - 10 * scale, startPosY + 86 * scale)
    drawCircle(john, 7 * scale, "white", "white", True)
    goto(john, startPosX + 0 * scale, startPosY + 86 * scale)
    drawCircle(john, 7 * scale, "white", "white", True)
    goto(john, startPosX + 10 * scale, startPosY + 86 * scale)
    drawCircle(john, 7 * scale, "white", "white", True)
    goto(john, startPosX + 20 * scale, startPosY + 86 * scale)
    drawCircle(john, 7 * scale, "white", "white", True)
    goto(john, startPosX + 0 * scale, startPosY + 125 * scale)
    drawCircle(john, 7 * scale, "white", "white", True)

    #arms
    goto(john, startPosX + 25 * scale, startPosY + 35 * scale)
    john.setheading(25)
    drawRectangle(john, 50 * scale, 7 * scale, "chocolate4", "chocolate4", True)
    goto(john, startPosX - 25 * scale, startPosY + 40 * scale)
    john.setheading(150)
    drawRectangle(john, 50 * scale, 7 * scale, "chocolate4", "chocolate4", True)

    #buttons
    goto(john, startPosX + 0 * scale, startPosY + 0 * scale)
    drawCircle(john, 2 * scale, "black", "black", True)
    goto(john, startPosX + 0 * scale, startPosY - 10 * scale)
    drawCircle(john, 2 * scale, "black", "black", True)
    goto(john, startPosX + 0 * scale, startPosY - 20 * scale)
    drawCircle(john, 2 * scale, "black", "black", True)
    goto(john, startPosX + 0 * scale, startPosY - 30 * scale)
    drawCircle(john, 2 * scale, "black", "black", True)
    goto(john, startPosX + 0 * scale, startPosY - 40 * scale)
    drawCircle(john, 2 * scale, "black", "black", True)
    goto(john, startPosX + 0 * scale, startPosY - 50 * scale)
    drawCircle(john, 2 * scale, "black", "black", True)
    goto(john, startPosX + 0 * scale, startPosY - 60 * scale)
    drawCircle(john, 2 * scale, "black", "black", True)

def geometricChristmasTree(drawArea, startPosX, startPosY, scale, color):
    john = turtle.RawTurtle(drawArea)
    john.hideturtle()
    john.speed(0)

    goto(john, startPosX + 0 * scale, startPosY + 0 * scale)
    drawTriangle(john, 30 * scale, color, color, True)
    goto(john, startPosX - 10 * scale, startPosY - 25 * scale)
    drawTriangle(john, 50 * scale, color, color, True)
    goto(john, startPosX - 15 * scale, startPosY - 45 * scale)
    drawTriangle(john, 60 * scale, color, color, True)

    goto(john, startPosX + 0 * scale, startPosY - 60 * scale)
    drawRectangle(john, 30 * scale, 15 * scale, "chocolate4", "chocolate4", True)

def finalCard(drawArea, startPosX, startPosY):
    john = turtle.RawTurtle(drawArea)
    john.hideturtle()
    john.speed(0)

    goto(john, startPosX + 0, startPosY + 0)
    drawRectangle(john, 600, 400, "#B6E7EE", "#B6E7EE", True)

    title(drawArea, -200, 100, 15)

    snowMan(drawArea, 0, -50, 1)
    snowStar(drawArea, 0, -20, 0.1)

    geometricChristmasTree(drawArea, 150, 125, 1, "green")
    geometricChristmasTree(drawArea, 200, 75, 1, "green")
    geometricChristmasTree(drawArea, 250, 100, 1, "green")

    fractalChristmasTree(drawArea, -200, -100,  50)
    starStyle2(drawArea, -200, 50, 0.1)

    startStyle1(drawArea, -250, 150, 0.35)
    startStyle1(drawArea, -125, -75, 0.35)
    startStyle1(drawArea, 25, 150, 0.35)
    startStyle1(drawArea, 175, -100, 0.35)