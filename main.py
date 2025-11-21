from graphics import Window, Line, Point


def main():
    win = Window(800, 600)
    # Draw a frame
    win.draw_line(Line(Point(20, 20), Point(780, 20)), "black")
    win.draw_line(Line(Point(780, 20), Point(780, 580)), "black")
    win.draw_line(Line(Point(780, 580), Point(20, 580)), "black")
    win.draw_line(Line(Point(20, 580), Point(20, 20)), "black")

    # Cross lines
    win.draw_line(Line(Point(20, 20), Point(780, 580)), "red")
    win.draw_line(Line(Point(780, 20), Point(20, 580)), "blue")

    # Some extra sample lines
    win.draw_line(Line(Point(100, 300), Point(700, 300)), "green")
    win.draw_line(Line(Point(400, 50), Point(400, 550)), "purple")

    # Ensure first render
    win.redraw()

    win.wait_for_close()

if __name__ == '__main__':
    main()


