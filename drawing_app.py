import turtle
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import xml.dom.minidom


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

    def __str__(self):
        return '<Command x="' + str(self.x) + '" y="' + str(self.y) + \
               '" width="' + str(self.width) + '" color="' + self.color + '">GoTo</Command>'


class CircleCommand:
    def __init__(self, radius, width=1, color="black"):
        self.radius = radius
        self.width = width
        self.color = color

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.circle(self.radius)

    def __str__(self):
        return '<Command radius="' + str(self.radius) + '" width="' + str(self.width) \
               + '" color="' + self.color + '">Circle</Command>'


class BeginFillCommand:
    def __init__(self, color):
        self.color = color

    def draw(self, turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()

    def __str__(self):
        return '<Command color="' + self.color + '">BeginFill</Command>'


class EndFillCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.end_fill()

    def __str__(self):
        return "<Command>EndFill</Command>"


class PenUpCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.penup()

    def __str__(self):
        return "<Command>PenUp</Command>"


class PenDownCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.pendown()

    def __str__(self):
        return "<Command>PenDown</Command>"


class PyList:
    def __init__(self):
        self.items = []

    def append(self, item):
        # self.items = self.items + [item]  # O(n^2)
        self.items.append(item)  # O(n)

    def remove_last(self):
        self.items = self.items[:-1]

    def __iter__(self):
        for c in self.items:
            yield c

    def __len__(self):
        return len(self.items)


class DrawingApplication(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.build_window()
        self.graphicsCommands = PyList()

    # This method is called to create all the widgets, place them in the GUI,
    # and define the event handlers for the application.
    def build_window(self):
        # the master is the root window
        self.master.title("Draw")

        bar = tkinter.Menu(self.master)
        file_menu = tkinter.Menu(bar, tearoff=0)     # tearoff=0 --> menus can’t be separated from the window

        # This code is called by the "New" menu item below when it is selected.
        # The same applies for loadFile, addToFile, and saveFile below. The
        # "Exit" menu item below calls quit on the "master" or root window.
        def new_window():
            # set up the turtle to be ready for a new picture to be drawn
            theTurtle.clear()
            theTurtle.penup()
            theTurtle.goto(0, 0)
            theTurtle.pendown()
            screen.update()
            screen.listen()
            self.graphicsCommands = PyList()

        file_menu.add_command(label="New", command=new_window)

        # The parse function adds the contents of an XML file to the sequence.
        def parse(filename):
            xmldoc = xml.dom.minidom.parse(filename)  # read the entire XML file

            graphics_commands_element = xmldoc.getElementsByTagName("GraphicsCommands")[0]
            graphics_commands = graphics_commands_element.getElementsByTagName("Command")

            for command_element in graphics_commands:
                print(type(command_element))
                command = command_element.firstChild.data.strip()
                attr = command_element.attributes
                if command == "GoTo":
                    x = float(attr["x"].value)
                    y = float(attr["y"].value)
                    width = float(attr["width"].value)
                    color = attr["color"].value.strip()
                    cmd = GoToCommand(x, y, width, color)

                elif command == "Circle":
                    radius = float(attr["radius"].value)
                    width = float(attr["width"].value)
                    color = attr["color"].value.strip()
                    cmd = CircleCommand(radius, width, color)

                elif command == "BeginFill":
                    color = attr["color"].value.strip()
                    cmd = BeginFillCommand(color)

                elif command == "EndFill":
                    cmd = EndFillCommand()

                elif command == "PenUp":
                    cmd = PenUpCommand()

                elif command == "PenDown":
                    cmd = PenDownCommand()

                else:
                    raise RuntimeError("Unknown Command: " + command)

                self.graphicsCommands.append(cmd)

        def load_file():

            filename = tkinter.filedialog.askopenfilename(title="Select a Graphics File")

            new_window()

            self.graphicsCommands = PyList()

            parse(filename)

            for cmd in self.graphicsCommands:
                cmd.draw(theTurtle)

            screen.update()

        file_menu.add_command(label="Load...", command=load_file)

        def add_to_file():

            filename = tkinter.filedialog.askopenfilename(title="Select a Graphics File")

            theTurtle.penup()
            theTurtle.goto(0, 0)
            theTurtle.pendown()
            theTurtle.pencolor("#000000")
            theTurtle.fillcolor("#000000")
            cmd = PenUpCommand()
            self.graphicsCommands.append(cmd)
            cmd = GoToCommand(0, 0, 1, "#000000")
            self.graphicsCommands.append(cmd)
            cmd = PenDownCommand()
            self.graphicsCommands.append(cmd)
            screen.update()
            parse(filename)

            for cmd in self.graphicsCommands:
                cmd.draw(theTurtle)

            screen.update()

        file_menu.add_command(label="Load Into...", command=add_to_file)

        def write(filename):
            file = open(filename, "w")
            file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
            file.write('<GraphicsCommands>\n')
            for cmd in self.graphicsCommands:
                file.write('   ' + str(cmd) + "\n")

            file.write('</GraphicsCommands>\n')
            file.close()

        def save_file():
            filename = tkinter.filedialog.asksaveasfilename(title="Save Picture As...")
            write(filename)
        file_menu.add_command(label="Save As...", command=save_file)

        file_menu.add_command(label="Exit", command=self.master.quit)

        bar.add_cascade(label="File", menu=file_menu)

        self.master.config(menu=bar)  # to display the newly created menu bar

        # The canvas is the drawing area on the left side of the window.
        canvas = tkinter.Canvas(self, width=600, height=600)
        canvas.pack(side=tkinter.LEFT)

        theTurtle = turtle.RawTurtle(canvas)
        theTurtle.shape('circle')
        screen = theTurtle.getscreen()

        screen.tracer(0)  # not update the screen unless screen.update() is called

        side_bar = tkinter.Frame(self, padx=5, pady=5)
        side_bar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

        point_label = tkinter.Label(side_bar, text="Width")
        point_label.pack()

        width_size = tkinter.StringVar()
        width_size.set(str(1))
        width_entry = tkinter.Entry(side_bar, textvariable=width_size)
        width_entry.pack()

        radius_label = tkinter.Label(side_bar, text="Radius")
        radius_label.pack()
        radius_size = tkinter.StringVar()
        radius_size.set(str(10))
        radius_entry = tkinter.Entry(side_bar, textvariable=radius_size)
        radius_entry.pack()

        # A button widget calls an event handler when it's pressed.
        def circle_handler():
            cmd = CircleCommand(float(radius_size.get()), float(width_size.get()), pen_color.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)

            screen.update()
            screen.listen()

        circle_button = tkinter.Button(side_bar, text="Draw Circle", command=circle_handler)
        circle_button.pack(fill=tkinter.BOTH)

        screen.colormode(255)  # color mode 255 - RGB form #RRGGBB
        pen_label = tkinter.Label(side_bar, text="Pen Color")
        pen_label.pack()
        pen_color = tkinter.StringVar()
        pen_color.set("#000000")    # black
        pen_entry = tkinter.Entry(side_bar, textvariable=pen_color)
        pen_entry.pack()

        def get_pen_color():
            color = tkinter.colorchooser.askcolor()
            # Comparisons to singletons like None should always be done with 'is' or 'is not'
            # never the equality operators
            if color is not None:
                pen_color.set(str(color)[-9:-2])

        pen_color_button = tkinter.Button(side_bar, text="Pick Pen Color", command=get_pen_color)
        pen_color_button.pack(fill=tkinter.BOTH)

        fill_label = tkinter.Label(side_bar, text="Fill Color")
        fill_label.pack()
        fill_color = tkinter.StringVar()
        fill_color.set("#000000")   # black
        fill_entry = tkinter.Entry(side_bar, textvariable=fill_color)
        fill_entry.pack()

        def get_fill_color():
            color = tkinter.colorchooser.askcolor()

            if color is not None:
                fill_color.set(str(color)[-9:-2])

        fill_color_button = tkinter.Button(side_bar, text="Pick Fill Color", command=get_fill_color)
        fill_color_button.pack(fill=tkinter.BOTH)

        def begin_fill_handler():
            cmd = BeginFillCommand(fill_color.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)

        begin_fill_button = tkinter.Button(side_bar, text="Begin Fill", command=begin_fill_handler)
        begin_fill_button.pack(fill=tkinter.BOTH)

        def end_fill_handler():
            cmd = EndFillCommand()
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)

        end_fill_button = tkinter.Button(side_bar, text="End Fill", command=end_fill_handler)
        end_fill_button.pack(fill=tkinter.BOTH)

        pen_label = tkinter.Label(side_bar, text="Pen Is Down")     #ZH
        pen_label.pack()

        def pen_up_handler():
            cmd = PenUpCommand()
            cmd.draw(theTurtle)
            pen_label.configure(text="Pen Is Up")
            self.graphicsCommands.append(cmd)

        pen_up_button = tkinter.Button(side_bar, text="Pen Up", command=pen_up_handler)
        pen_up_button.pack(fill=tkinter.BOTH)

        def pen_down_handler():
            cmd = PenDownCommand()
            cmd.draw(theTurtle)
            pen_label.configure(text="Pen Is Down")
            self.graphicsCommands.append(cmd)

        pen_down_button = tkinter.Button(side_bar, text="Pen Down", command=pen_down_handler)
        pen_down_button.pack(fill=tkinter.BOTH)

        # mouse click handler
        def click_handler(x, y):
            cmd = GoToCommand(x, y, float(width_size.get()), pen_color.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()

        screen.onclick(click_handler)

        def drag_handler(x, y):
            cmd = GoToCommand(x, y, float(width_size.get()), pen_color.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()

        theTurtle.ondrag(drag_handler)

        # undo the last command
        # remove it from the sequence and redraw the entire picture
        def undo_handler():
            if len(self.graphicsCommands) > 0:
                self.graphicsCommands.remove_last()
                theTurtle.clear()
                theTurtle.penup()
                theTurtle.goto(0, 0)
                theTurtle.pendown()

                for cmd in self.graphicsCommands:
                    cmd.draw(theTurtle)
                screen.update()
                screen.listen()

        screen.onkeypress(undo_handler, "u")
        screen.listen()


def main():
    root = tkinter.Tk()
    drawingApp = DrawingApplication(root)

    drawingApp.mainloop()  # start listening for events
    print("Program Execution Completed.")


if __name__ == "__main__":
    main()
