import turtle
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import xml.dom.minidom
import math
import sys

class PlotApplication(tkinter.Frame):
    def __init__(self, master=None, datafile=None):
        super().__init__(master)
        self.datafile = datafile
        self.pack()
        self.build_window()

    def build_window(self):
        self.master.title("Plot")

        bar = tkinter.Menu(self.master)
        file_menu = tkinter.Menu(bar, tearoff=0)

        def load_file(filename=None):
            if filename is None:
                filename = tkinter.filedialog.askopenfilename(title="Select a Plot File")

            the_turtle.clear()
            the_turtle.penup()
            the_turtle.goto(0, 0)
            the_turtle.pendown()
            screen.update()
            the_turtle.color("black")

            xml_doc = xml.dom.minidom.parse(filename)

            plot_element = xml_doc.getElementsByTagName("Plot")[0]

            attr = plot_element.attributes
            self.master.title(attr["title"].value)

            axes_element = plot_element.getElementsByTagName("Axes")[0]

            x_axis_element = axes_element.getElementsByTagName("XAxis")[0]
            y_axis_element = axes_element.getElementsByTagName("YAxis")[0]

            x_axis_label = x_axis_element.firstChild.data.strip()
            y_axis_label = y_axis_element.firstChild.data.strip()

            x_attr = x_axis_element.attributes
            y_attr = y_axis_element.attributes

            min_x = float(x_attr["min"].value)
            max_x = float(x_attr["max"].value)
            min_y = float(y_attr["min"].value)
            max_y = float(y_attr["max"].value)

            x_size = max_x - min_x
            y_size = max_y - min_y
            x_center = x_size/2.0 + min_x
            y_center = y_size/2.0 + min_y

            # number of decimal places to display
            x_places = max(4-round(math.log(x_size, 10)), 0)
            y_places = max(4-round(math.log(y_size, 10)), 0)

            label_y_val = max_y - 0.10 * y_size  # y value of sequence title

            screen.setworldcoordinates(min_x-0.20*x_size, min_y-0.20*y_size,
                                       max_x+0.20*x_size, max_y+0.20*y_size)

            the_turtle.ht()  # ht: hideturtle

            the_turtle.penup()
            the_turtle.goto(min_x, min_y)
            the_turtle.pendown()
            the_turtle.goto(max_x, min_y)
            the_turtle.penup()
            the_turtle.goto(min_x, min_y)
            the_turtle.pendown()
            the_turtle.goto(min_x, max_y)
            the_turtle.penup()

            the_turtle.goto(x_center, min_y-0.10*y_size)
            the_turtle.write(x_axis_label, align="center", font=("Arial", 14, "bold"))

            the_turtle.goto(min_x, max_y+0.05*y_size)
            the_turtle.write(y_axis_label, align="center", font=("Arial", 14, "bold"))

            for i in range(0, 101, 10):
                x = min_x + x_size * i / 100.0
                y = min_y + y_size * i / 100.0

                the_turtle.penup()
                the_turtle.goto(x, min_y+y_size*0.025)
                the_turtle.pendown()
                the_turtle.goto(x, min_y-y_size*0.025)
                the_turtle.penup()
                the_turtle.goto(x, min_y-y_size*0.05)

                the_turtle.write(("%1."+str(x_places)+"f") % x, align="center", font=("Arial", 12, "normal"))

                the_turtle.penup()
                the_turtle.goto(min_x+x_size*0.025, y)
                the_turtle.pendown()
                the_turtle.goto(min_x-x_size*0.025, y)
                the_turtle.penup()
                the_turtle.goto(min_x-x_size*0.001, y)

                the_turtle.write(("%1."+str(y_places)+"f") % y, align="right", font=("Arial", 12, "normal"))

            sequences = plot_element.getElementsByTagName("Sequence")

            for sequence in sequences:
                attr = sequence.attributes

                label = attr["title"].value.strip()
                color = attr["color"].value
                the_turtle.color(color)
                the_turtle.penup()
                the_turtle.goto(x_center, label_y_val)
                label_y_val = label_y_val - 0.1 * y_size  # update y value for next sequence's title
                the_turtle.write(label, align="center", font=("Arial", 18, "bold"))

                data_points = sequence.getElementsByTagName("DataPoint")

                first = data_points[0]
                attr = first.attributes
                x = float(attr["x"].value)
                y = float(attr["y"].value)
                the_turtle.goto(x, y)
                the_turtle.dot()
                the_turtle.pendown()

                for data_point in data_points:
                    attr = data_point.attributes
                    x = float(attr["x"].value)
                    y = float(attr["y"].value)
                    the_turtle.goto(x, y)
                    the_turtle.dot()

                screen.update()

        file_menu.add_command(label="Load Plot Data...", command=load_file)
        file_menu.add_command(label="Exit", command=self.master.quit)

        bar.add_cascade(label="File", menu=file_menu)
        self.master.config(menu=bar)

        canvas = tkinter.Canvas(self, width=1000, height=800)
        canvas.pack(side=tkinter.LEFT)

        the_turtle = turtle.RawTurtle(canvas)
        screen = the_turtle.getscreen()
        screen.tracer(0)

        if self.datafile is not None:
            load_file(self.datafile.strip())


def main():
    root = tkinter.Tk()
    datafile = None
    if len(sys.argv) > 1:
        datafile = sys.argv[1]
    plot_app = PlotApplication(root, datafile)
    plot_app.mainloop()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main()