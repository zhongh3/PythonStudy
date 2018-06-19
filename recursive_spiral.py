import turtle


def draw_spiral(t, length, color, color_base):
    if length == 0:
        return

    # color[0] is "#"
    new_color = (int(color[1:], 16) + 2 ** 10) % (2 ** 24)
    base = int(color_base[1:], 16)

    if new_color < base:
        new_color = (new_color + base) % (2 ** 24)

    new_color = hex(new_color)[2:]  # hex(new_color) - '0xAAA'

    new_color = "#" + ("0" * (6 - len(new_color))) + new_color

    t.color(new_color)
    t.forward(length)
    t.left(90)

    draw_spiral(t, length-1, new_color, color_base)


def main():
    t = turtle.Turtle()
    screen = t.getscreen()
    t.speed(100)
    t.penup()
    t.goto(-100, -100)
    t.pendown()

    draw_spiral(t, 200, "#000000", "#00ff00")

    screen.exitonclick()


if __name__ == "__main__":
    main()

