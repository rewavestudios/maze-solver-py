from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height, title=None):
        self.__root = Tk()
        # default title, override if provided
        self.__root.title("Maze Solver" if title is None else title)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        # track last cell used for drawing moves
        self.__last_cell = None

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def draw_move(self, to_cell, undo=False):
        """Draw a move between two cells.

        If `from_cell` is None, the method will use the internally tracked
        last cell (`self.__last_cell`). If there's no known from-cell, the
        call will set the last cell and return without drawing.

        `undo` controls color: red for forward moves, gray for undo/backtrack.
        """
        # determine source cell (use internally tracked last cell)
        src = self.__last_cell
        # if we don't have a source yet, store and exit
        if src is None:
            self.__last_cell = to_cell
            return

        # compute centers
        try:
            sx, sy = src.center()
            tx, ty = to_cell.center()
        except Exception:
            # if cells don't expose center(), try access mangled attributes
            sx = (src._Cell__x1 + src._Cell__x2) // 2
            sy = (src._Cell__y1 + src._Cell__y2) // 2
            tx = (to_cell._Cell__x1 + to_cell._Cell__x2) // 2
            ty = (to_cell._Cell__y1 + to_cell._Cell__y2) // 2

        color = "gray" if undo else "red"
        p1 = Point(sx, sy)
        p2 = Point(tx, ty)
        self.draw_line(Line(p1, p2), color)

        # update last cell
        if not undo:
            self.__last_cell = to_cell

    def close(self):
        self.__running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(
        self,
        p1,
        p2,
    ):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(self, win):
        # wall flags
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        # coordinates (pixel bounds)
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1

        # reference to Window instance (used to draw)
        self.__win = win

    def draw(self, x1, y1, x2, y2, wall_color="black"):
        """Update internal coordinates and draw walls based on flags.

        Coordinates are pixel positions where (x1,y1) is top-left and
        (x2,y2) is bottom-right of the cell.
        """
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        # Left wall: from (x1,y1) to (x1,y2)
        if self.has_left_wall:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x1, self.__y2)
            self.__win.draw_line(Line(p1, p2), wall_color)

        # Top wall: from (x1,y1) to (x2,y1)
        if self.has_top_wall:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x2, self.__y1)
            self.__win.draw_line(Line(p1, p2), wall_color)

        # Right wall: from (x2,y1) to (x2,y2)
        if self.has_right_wall:
            p1 = Point(self.__x2, self.__y1)
            p2 = Point(self.__x2, self.__y2)
            self.__win.draw_line(Line(p1, p2), wall_color)

        # Bottom wall: from (x1,y2) to (x2,y2)
        if self.has_bottom_wall:
            p1 = Point(self.__x1, self.__y2)
            p2 = Point(self.__x2, self.__y2)
            self.__win.draw_line(Line(p1, p2), wall_color)

    def center(self):
        """Return the center pixel coordinates (cx, cy) of this cell."""
        cx = (self.__x1 + self.__x2) // 2
        cy = (self.__y1 + self.__y2) // 2
        return cx, cy
