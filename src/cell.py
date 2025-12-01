from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        # allow win to be optional for unit testing (no drawing)
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win

    def draw(self, x1, y1, x2, y2, wall_color="black", bg_color=None):
        """Update internal coordinates and draw walls.

        If `bg_color` is provided, walls that are absent will be drawn using
        `bg_color` to erase previously drawn lines. If no `bg_color` is
        provided we default to `white` (the Canvas background used by demos).
        """
        # Always update internal coordinates so logic can be unit-tested
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        # If no window provided, skip actual drawing
        if self.__win is None:
            return

        bg = "white" if bg_color is None else bg_color

        # draw each wall; if the wall flag is False, draw over it with bg color
        color = wall_color if self.has_left_wall else bg
        line = Line(Point(x1, y1), Point(x1, y2))
        self.__win.draw_line(line, color)

        color = wall_color if self.has_top_wall else bg
        line = Line(Point(x1, y1), Point(x2, y1))
        self.__win.draw_line(line, color)

        color = wall_color if self.has_right_wall else bg
        line = Line(Point(x2, y1), Point(x2, y2))
        self.__win.draw_line(line, color)

        color = wall_color if self.has_bottom_wall else bg
        line = Line(Point(x1, y2), Point(x2, y2))
        self.__win.draw_line(line, color)

    def center(self):
        """Return center (cx, cy) of this cell (handles rectangular cells)."""
        cx = (self.__x1 + self.__x2) // 2
        cy = (self.__y1 + self.__y2) // 2
        return cx, cy

    def draw_move(self, to_cell, undo=False):
        # compute centers for both cells (handle rectangular cells)
        try:
            x_center, y_center = self.center()
            x_center2, y_center2 = to_cell.center()
        except Exception:
            # fallback to direct attribute access if needed
            half_x = abs(self.__x2 - self.__x1) // 2
            half_y = abs(self.__y2 - self.__y1) // 2
            x_center = self.__x1 + half_x
            y_center = self.__y1 + half_y

            half_x2 = abs(to_cell.__x2 - to_cell.__x1) // 2
            half_y2 = abs(to_cell.__y2 - to_cell.__y1) // 2
            x_center2 = to_cell.__x1 + half_x2
            y_center2 = to_cell.__y1 + half_y2

        fill_color = "red" if not undo else "gray"

        # If no window, skip drawing but still run calculation logic
        if self.__win is None:
            return

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self.__win.draw_line(line, fill_color)
