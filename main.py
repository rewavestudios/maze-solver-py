from graphics import Window, Point, Line, Cell


def main():
    win = Window(800, 600)

    # Draw a few cells with different wall configurations
    c1 = Cell(win)
    # default: all walls
    c1.draw(50, 50, 150, 150, "black")

    c2 = Cell(win)
    # open top
    c2.has_top_wall = False
    c2.draw(170, 50, 270, 150, "black")

    c3 = Cell(win)
    # open left and bottom
    c3.has_left_wall = False
    c3.has_bottom_wall = False
    c3.draw(50, 170, 150, 270, "black")

    c4 = Cell(win)
    # open right
    c4.has_right_wall = False
    c4.draw(170, 170, 270, 270, "black")

    # Render once then wait for close
    win.redraw()
    win.wait_for_close()


if __name__ == '__main__':
    main()

