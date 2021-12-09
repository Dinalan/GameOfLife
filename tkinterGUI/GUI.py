from tkinter import *
from math import floor
import time

from tkinterGUI.EventHandler import EventHandler
from bg.Grid import Grid, BetterGrid


class GUI:
    def __init__(self):
        self.data = {
            "gridtype": "Grid",
            "gridsize": "100x100",
            "tilesize": 5,
            "winsize": "1000x800",
            "spawnchance": 50,
            "refreshrate": 1000,
            "outline": True,
            "rainbow": False,
            "running": False
        }

        self.evnthdlr = EventHandler(self)
        self.m1pressed = False
        self.to_draw = []
        self.rainbowcolors = [
            "#AA0000", "#FF5000", "#AAAA00", "#00AA00", "#50AAAA", "#0000AA",
            "#9400D3"
        ]
        self.lastcolorindex = 0

    def start(self):
        self.tk = Tk()

        self.tk.title("GameOfLife - Setup")
        #self.tk.geometry("500x400")
        #self.tk.resizable(False, False)

        gridtypes_options = ["BetterGrid", "Grid"]
        gridsize_tilesize_options = [
            "100x100-8", "100x100-6", "100x100-4", "100x100-2", "200x200-4",
            "200x200-2", "300x300-2", "400x400-2"
        ]
        refreshrate_options = [
            1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 50, 1
        ]
        self.gdt_var = StringVar(self.tk)
        self.gdt_var.set(gridtypes_options[0])

        self.gsts_var = StringVar(self.tk)
        self.gsts_var.set(gridsize_tilesize_options[0])

        self.rfrsh_var = IntVar(self.tk)
        self.rfrsh_var.set(refreshrate_options[0])

        self.outline_var = BooleanVar(self.tk)

        self.rainbow_var = BooleanVar(self.tk)

        self.gdt_menu = OptionMenu(self.tk, self.gdt_var, *gridtypes_options)
        self.gdt_menu.config(width=8, font=('Helvetica', 10))

        self.gsts_menu = OptionMenu(self.tk, self.gsts_var,
                                    *gridsize_tilesize_options)
        self.gsts_menu.config(width=8, font=('Helvetica', 10))

        self.rfrsh_menu = OptionMenu(self.tk, self.rfrsh_var,
                                     *refreshrate_options)
        self.rfrsh_menu.config(width=8, font=('Helvetica', 10))

        self.spawnchance_spin = Spinbox(self.tk, from_=0, to=100)

        self.outline_chkbtn = Checkbutton(self.tk,
                                          text="Outline",
                                          variable=self.outline_var,
                                          onvalue=True,
                                          offvalue=False)
        self.rainbow_chkbtn = Checkbutton(self.tk,
                                          text="RAINBOW !!!",
                                          variable=self.rainbow_var,
                                          onvalue=True,
                                          offvalue=False)
        self.outline_chkbtn.select()

        self.gdt_label = Label(self.tk,
                               text="Choose grid type (BetterGrid = better)")
        self.gsts_label = Label(self.tk, text="Choose your resolution (GS-TS)")
        self.rfrsh_label = Label(self.tk, text="Choose your refresh rate (ms)")
        self.spawnchance_label = Label(self.tk, text="Choose the spawnchance")

        self.launch_btn = Button(self.tk,
                                 text="Run",
                                 command=self.evnthdlr.handle_run)
        self.launch_btn.config(width=12, height=3, font=('Helvetica', 11))

        self.gdt_label.grid(row=0, column=0)
        self.gdt_menu.grid(row=0, column=1)

        self.gsts_label.grid(row=1, column=0)
        self.gsts_menu.grid(row=1, column=1)

        self.rfrsh_label.grid(row=2, column=0)
        self.rfrsh_menu.grid(row=2, column=1)

        self.spawnchance_label.grid(row=3, column=0)
        self.spawnchance_spin.grid(row=3, column=1)

        self.outline_chkbtn.grid(row=4, column=1)

        self.rainbow_chkbtn.grid(row=6, column=1)

        self.launch_btn.grid(row=5, column=1, pady=(5, 10))

        self.tk.mainloop()

    def delete_init(self):
        self.tk.destroy()
        del self.tk
        del self.gsts_var
        del self.gsts_menu
        del self.gsts_label
        del self.rfrsh_var
        del self.rfrsh_menu
        del self.rfrsh_label
        del self.spawnchance_label
        del self.spawnchance_spin
        del self.launch_btn
        del self.gdt_var
        del self.gdt_menu
        del self.gdt_label
        del self.outline_var
        del self.outline_chkbtn

    def init_run(self):
        self.tk = Tk()

        self.tk.title("GameOfLife - Running")
        # self.tk.geometry(self.data["winsize"])
        # self.tk.resizable(False, False)

        self.xsize = int(self.data["gridsize"].split("x")[0])
        self.ysize = int(self.data["gridsize"].split("x")[1])
        print("size", self.xsize, self.ysize)

        self.cnvs = Canvas(self.tk,
                           width=self.xsize * self.data["tilesize"],
                           height=self.ysize * self.data["tilesize"],
                           bg="black")

        if self.data["gridtype"] == "BetterGrid":
            self.grid = BetterGrid((self.xsize, self.ysize),
                                   self.data["spawnchance"])
        else:
            self.grid = Grid(self.xsize,
                             self.ysize,
                             spawnchance=self.data["spawnchance"])

        self.data_var = StringVar(self.tk)
        #self.data_var.set()
        self.data_label = Label(self.tk, textvariable=self.data_var)

        self.calculationtime_var = StringVar(self.tk)
        self.lasttimedraw = 0
        self.lasttimeupdate = 0
        self.calculationtime_label = Label(
            self.tk, textvariable=self.calculationtime_var)

        self.tk.bind("<space>", self.evnthdlr.handle_switch)
        self.tk.bind("<Escape>", self.evnthdlr.handle_reset)
        self.tk.bind("<ButtonPress-1>", self.evnthdlr.handle_m1pressed)
        self.tk.bind("<ButtonRelease-1>", self.evnthdlr.handle_m1released)
        self.tk.bind("<Motion>", self.evnthdlr.motion)

    def run(self):
        self.draw()
        self.tk.after(10, self.update)
        self.tk.focus_force()
        self.tk.mainloop()

    def update(self):
        if self.data["running"]:
            self.lasttimeupdate = time.time()
            self.grid.update()
            self.lasttimeupdate = str(
                int((time.time() - self.lasttimeupdate) * 1000))
            self.lasttimedraw = time.time()
            self.draw()
            self.lasttimedraw = str(
                int((time.time() - self.lasttimedraw) * 1000))

            # WARNING: BARBARIANS WERE THERE NOT SO LONG AGO !
            self.calculationtime_var.set(
                "Update: " + self.lasttimeupdate + "ms\nDraw: " +
                self.lasttimedraw + "ms\nTotal calculation time: " +
                str(int(self.lasttimeupdate) + int(self.lasttimedraw)) + " ms")

        self.calculationtime_label.grid(row=1, column=0)
        self.tk.after(self.data["refreshrate"], self.update)

    def draw(self):

        if self.data["rainbow"]:
            if self.lastcolorindex >= len(self.rainbowcolors):
                self.lastcolorindex = 0
            color = self.rainbowcolors[self.lastcolorindex]
            self.lastcolorindex += 1
        else:
            color = "white"

        self.cnvs.delete("all")
        x = 0
        y = 0

        grid = self.grid.getgrid()

        for pos in self.to_draw:
            posgrid = (floor(pos[0] / self.data["tilesize"]),
                       floor(pos[1] / self.data["tilesize"]))

            grid[posgrid[1]][posgrid[0]] = 1
            self.to_draw.remove(pos)

        for i in range(self.ysize):
            for j in range(self.xsize):
                if grid[i][j] == 1:
                    if self.data["outline"]:
                        self.cnvs.create_rectangle(x,
                                                   y,
                                                   x + self.data["tilesize"],
                                                   y + self.data["tilesize"],
                                                   fill=color)
                    else:
                        self.cnvs.create_rectangle(x,
                                                   y,
                                                   x + self.data["tilesize"],
                                                   y + self.data["tilesize"],
                                                   fill=color,
                                                   outline=color)
                x += self.data["tilesize"]
            y += self.data["tilesize"]
            x = 0

        self.cnvs.grid(row=0, column=0)

    def delete_run(self):
        self.tk.destroy()
        del self.tk
        del self.cnvs
        del self.grid
        del self.xsize
        del self.ysize
        del self.calculationtime_label
        del self.calculationtime_var
        del self.lasttimeupdate
        del self.lasttimedraw


if __name__ == '__main__':
    g = GUI()
    g.start()
