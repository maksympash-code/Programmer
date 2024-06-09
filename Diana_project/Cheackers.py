from tkinter import *
from PIL import Image, ImageTk

class BoundObj:
    def __init__(self, master, row, col, obj, img, **features):
        self.master = master
        self.row = row
        self.col = col
        self.obj = obj
        self.img = img
        self.features = features

    def draw(self, width, height, ratio):
        left = self.col * width
        top = self.row * height
        self.id = self.obj.draw(self.master, left, top, width, height, ratio, self.img)


class BoundOval:
    def __init__(self):
        pass

    def draw(self, master, left, top, width, height, ratio, img):
        xmin = left + (width * (1 - ratio)) / 2
        ymin = top + (height * (1 - ratio)) / 2
        img = master.create_image(xmin, ymin, anchor=NW, image=img)
        return img


class GridCanvas(Canvas):
    def __init__(self, master, rows, cols, selection_handler, *args, bordercolor='black', evenbg='', ratio=0.85, highlightbg='grey', **kwargs):
        Canvas.__init__(self, master, *args, **kwargs)
        self.rows = rows
        self.cols = cols
        self.selection_handler = selection_handler
        self.bordercolor = bordercolor
        self.evenbg = evenbg
        self.highlightbg = highlightbg
        self.ratio = ratio
        self.cellwidth = int(self['width']) // self.cols
        self.cellheight = int(self['height']) // self.rows
        self.grid = []
        for row in range(rows):
            self.grid.append([])
            for col in range(cols):
                self.grid[row].append(None)
        self._drawgrid()
        self.bind('<Button-1>', self.on_click)
        self.moved = IntVar()
        self.moved.set(1)

    def _tagstr(self, row, col):
        return 't{:0>3}{:0>3}'.format(row, col)

    def _drawgrid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                xstart = col * self.cellwidth
                ystart = row * self.cellheight
                xend = xstart + self.cellwidth + 1
                yend = ystart + self.cellheight + 1
                if self.evenbg and (row + col) % 2 == 0:
                    bg = self.evenbg
                else:
                    bg = self['bg']
                self.create_rectangle(xstart, ystart, xend, yend, width=self['bd'], fill=bg, outline=self.bordercolor, tags=self._tagstr(row, col))

    def create_bound(self, row, col, obj, img, **features):
        self.grid[row][col] = BoundObj(self, row, col, obj, img, **features)
        self.grid[row][col].draw(self.cellwidth, self.cellheight, self.ratio)
        self.tag_raise(self.grid[row][col].id)  # Піднімаємо створену шашку на передній план

    def delete_bound(self, row, col):
        bo = self.grid[row][col]
        if bo:
            self.delete(bo.id)
            self.grid[row][col] = None

    def _movestep(self, id, ddx, ddy, xfinal, yfinal):
        x, y, mx, my = self.coords(id)
        if x == xfinal:
            ddx = 0
        if y == yfinal:
            ddy = 0
        if ddx or ddy:
            self.move(id, ddx, ddy)
            self.after(5, self._movestep, id, ddx, ddy, xfinal, yfinal)
        else:
            self.moved.set(1)

    def move_bound(self, fromrow, fromcol, torow, tocol, slow=False):
        dx = (tocol - fromcol) * self.cellwidth
        dy = (torow - fromrow) * self.cellheight
        bo = self.grid[fromrow][fromcol]
        if bo and (dx != 0 or dy != 0):
            self.tag_raise(bo.id)  # Піднімаємо шашку на передній план перед рухом
            if slow:
                ddx = _sign(dx)
                ddy = _sign(dy)
                xfinal = tocol * self.cellwidth + int(self.cellwidth * (1 - self.ratio) / 2)
                yfinal = torow * self.cellheight + int(self.cellheight * (1 - self.ratio) / 2)
                self.moved.set(0)
                self._movestep(bo.id, ddx, ddy, xfinal, yfinal)
                self.wait_variable(self.moved)
            else:
                self.move(bo.id, dx, dy)
            self.grid[fromrow][fromcol] = None
            bo.row, bo.col = torow, tocol
            self.grid[torow][tocol] = bo

    def select_cell(self, row, col):
        self.itemconfigure(self._tagstr(row, col), fill=self.highlightbg)

    def deselect_cell(self, row, col):
        if self.evenbg and (row + col) % 2 == 0:
            bg = self.evenbg
        else:
            bg = self['bg']
        self.itemconfigure(self._tagstr(row, col), fill=bg)

    def on_click(self, ev):
        if self.moved.get():
            x = self.canvasx(ev.x)
            y = self.canvasy(ev.y)
            row = min(int(y) // self.cellheight, self.rows - 1)
            col = min(int(x) // self.cellwidth, self.cols - 1)
            self.selection_handler(self, row, col)


def _sign(val):
    if val > 0:
        sign = 1
    elif val == 0:
        sign = 0
    else:
        sign = -1
    return sign


lastrow, lastcol = None, None
selected_piece = None
turn = 'white'
must_continue_capture = False


def sel_handler(gc, row, col):
    global lastrow, lastcol, selected_piece, turn, must_continue_capture
    piece = gc.grid[row][col]
    if selected_piece:
        if piece is None or piece.img != selected_piece.img:
            if valid_move(gc, selected_piece, row, col):
                if abs(lastrow - row) == 2:
                    mid_row = (lastrow + row) // 2
                    mid_col = (lastcol + col) // 2
                    gc.delete_bound(mid_row, mid_col)
                    must_continue_capture = can_continue_capture(gc, selected_piece, row, col)
                gc.move_bound(lastrow, lastcol, row, col, slow=True)
                if not must_continue_capture:
                    switch_turn()
                else:
                    lastrow, lastcol = row, col
                    return
            gc.deselect_cell(lastrow, lastcol)
            selected_piece = None
        else:
            gc.deselect_cell(lastrow, lastcol)
            gc.select_cell(row, col)
            lastrow, lastcol = row, col
            selected_piece = piece
    else:
        if piece and piece.img == turn:
            gc.select_cell(row, col)
            lastrow, lastcol = row, col
            selected_piece = piece


def switch_turn():
    global turn, must_continue_capture
    turn = 'white' if turn == 'black' else 'black'
    must_continue_capture = False


def valid_move(gc, piece, row, col):
    if gc.grid[row][col] is not None:
        return False  # Заборона ходити на клітинку, де вже є шашка
    dr = row - piece.row
    dc = col - piece.col
    # Дозволяємо бити назад, але забороняємо звичайні ходи назад
    if abs(dr) == abs(dc) == 1:
        if piece.img == 'white' and dr <= 0:
            return False
        if piece.img == 'black' and dr >= 0:
            return False
        return True
    if abs(dr) == abs(dc) == 2:
        mid_row = (piece.row + row) // 2
        mid_col = (piece.col + col) // 2
        mid_piece = gc.grid[mid_row][mid_col]
        return mid_piece and mid_piece.img != piece.img
    return False


def can_continue_capture(gc, piece, row, col):
    directions = [(-2, -2), (-2, 2), (2, -2), (2, 2)]
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < gc.rows and 0 <= new_col < gc.cols:
            if valid_move(gc, piece, new_row, new_col):
                return True
    return False


def main():
    top = Tk()
    cell_width, cell_height = 350 // 8, 350 // 8

    white_piece_img = Image.open('img.png')
    white_piece_img = white_piece_img.resize((int(cell_width * 0.85), int(cell_height * 0.85)), Image.LANCZOS)
    white_piece_img = ImageTk.PhotoImage(white_piece_img)

    black_piece_img = Image.open('img_1.png')
    black_piece_img = black_piece_img.resize((int(cell_width * 0.85), int(cell_height * 0.85)), Image.LANCZOS)
    black_piece_img = ImageTk.PhotoImage(black_piece_img)

    gc = GridCanvas(top, 8, 8, sel_handler, bordercolor='grey', evenbg='white', width=350, height=350, bg='black', bd=2)
    gc.pack()
    for row in range(3):
        for col in range(8):
            if (row + col) % 2 == 1:
                gc.create_bound(row, col, BoundOval(), img=white_piece_img)
    for row in range(5, 8):
        for col in range(8):
            if (row + col) % 2 == 1:
                gc.create_bound(row, col, BoundOval(), img=black_piece_img)
    mainloop()


if __name__ == '__main__':
    main()
