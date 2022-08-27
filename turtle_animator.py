import turtle as t
import colorsys
import sys


def help():
    print("Usage: python3 tutle.py [options]")
    print("Options:")
    print("  -h, --help\t\tShow this help message and exit")
    print("  -bc, --baseColor\t\tBase Color Integer")
    print("  -bgc, --backGroundColor\t\tBase Color of the turtle")
    print("  -s, --speed\t\tSpeed of the turtle")
    print("  -cs, --circleSize\tSize of the circle")
    print("  -d, --devider\t\tDevider for Color adjustment (c/d)/ draw cycle")
    print("  -is, --innerSpace\tSpace inside")
    print("  -rau, --rotationAngleUnits\tRotation Angle Units (degrees)")
    print("  -spr, --shiftPerRepetiton\tShift per Repetition")	
    print("  -r, --repetition\tRepetition of cycles")
    exit(0)


def drawTurtle(repetitions, devider, speed, backGroundColor, circleSize, shiftPerRepetition, innerSpace, rotationAngleUnits, baseColor):
    WIDTH = HEIGHT = .8
    screen = t.Screen()
    screen.setup(WIDTH, HEIGHT)  
    screen.screensize(WIDTH, HEIGHT) 
    turtle = t.Turtle()
    turtle.screen.bgcolor(backGroundColor)
    turtle.speed(speed)
    for i in range(repetitions):
        color = colorsys.hsv_to_rgb(baseColor, 1, 0.9)
        baseColor += 1/devider
        turtle.color(color)
        turtle.forward(shiftPerRepetition)
        for i in range(5):
            turtle.circle(circleSize)
            turtle.left(rotationAngleUnits)
            turtle.forward(innerSpace)
            


    turtle.hideturtle()
    input("Press Enter to exit")


if __name__ == '__main__':
    
    backGroundColor = "black"
    speed = 50
    circleSize = 100
    devider = 22
    innerSpace = 100
    shiftPerRepetition = 0
    repetitions = 10
    rotationAngleUnits = 100
    baseColor = 0
    arguments = sys.argv[1:]
    for element in arguments:
        if(element == "-h" or element == "--help"):
            help()
        elif(element == "-bc" or element == "--baseColor"):
            baseColor = int(arguments[arguments.index(element)+1])
        elif(element == "-bgc" or element == "--backGroundColor"):
            backGroundColor = arguments[arguments.index(element)+1]
        elif(element == "-s" or element == "--speed"):
            speed = int(arguments[arguments.index(element)+1])
        elif(element == "-cs" or element == "--circleSize"):
            circleSize = int(arguments[arguments.index(element)+1])
        elif(element == "-d" or element == "--devider"):
            devider = int(arguments[arguments.index(element)+1])
        elif(element == "-ics" or element == "--innerCircleShift"):
            innerSpace = int(arguments[arguments.index(element)+1])
        elif(element == "-rau" or element == "--rotationAngleUnits"):
            rotationAngleUnits = int(arguments[arguments.index(element)+1])
        elif(element == "-r" or element == "--repetition"):
            repetitions = int(arguments[arguments.index(element)+1])

    print("Base Color: " + str(baseColor))
    print("Background Color: " + backGroundColor)
    print("Speed: " + str(speed))
    print("Circle Size: " + str(circleSize))
    print("Devider: " + str(devider))
    print("Inner Space: " + str(innerSpace))
    print("Shift per Repetition: " + str(shiftPerRepetition))
    print("Rotation Angle Units: " + str(rotationAngleUnits))
    print("Repetitions: " + str(repetitions))

    drawTurtle(repetitions=repetitions, devider=devider, speed=speed, backGroundColor=backGroundColor,
               circleSize=circleSize, innerSpace=innerSpace,
               shiftPerRepetition=shiftPerRepetition,
               rotationAngleUnits=rotationAngleUnits, baseColor=baseColor)
    
