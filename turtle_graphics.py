import turtle


class GoToCommand:
    def __init__(self, x, y, width=1, color="black"):
        self.x = x
        self.y = y
        self.width = width
        self.color = color

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x, self.y)


class CircleCommand:
    def __init__(self, radius, width=1, color="black"):
        self.radius = radius
        self.width = width
        self.color = color

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.circle(self.radius)


class BeginFillCommand:
    def __init__(self, color):
        self.color = color

    def draw(self, turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()


class EndFillCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.end_fill()


class PenUpCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.penup()


class PenDownCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.pendown()


class PyList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items = self.items + [item]

    def __iter__(self):
        for c in self.items:
            yield c


def main():
    filename = input("please enter drawing filename: ")

    #create a Turtle Graphics window
    t = turtle.Turtle()

    screen = t.getscreen()

    file = open(filename, "r")

    graphics_commands = PyList()

    command = file.readline().strip()

    while command != "":

        if command == "goto":
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = GoToCommand(x, y, width, color)

        elif command == "circle":
            radius = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = CircleCommand(radius, width, color)

        elif command == "beginfill":
            color = file.readline().strip()
            cmd = BeginFillCommand(color)

        elif command == "endfill":
            cmd = EndFillCommand()

        elif command == "penup":
            cmd = PenUpCommand()

        elif command == "pendown":
            cmd = PenDownCommand()

        else:
            raise RuntimeError("Unknown Command: " + command)

        graphics_commands.append(cmd)

        command = file.readline().strip()

    for cmd in graphics_commands:
        cmd.draw(t)

    # close the file
    file.close()

    # hide the turtle
    t.ht()

    # hold the Turtle Graphics window open until the mouse is clicked
    screen.exitonclick()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main()