class EventHandler:

    def __init__(self, master):
        self.master = master

    def handle_run(self, event=False):
        print(f"Run request with:\n   gdt_var = {self.master.gdt_var.get()}\
                                \n   gsts_var = {self.master.gsts_var.get()}\
                                \n   rfrsh_var = {self.master.rfrsh_var.get()}\
                                \n   spawnchance = {self.master.spawnchance_spin.get()}")

        splitted_tsgs = self.master.gsts_var.get().split("-")
        self.master.data["gridsize"] = splitted_tsgs[0]
        self.master.data["tilesize"] = int(splitted_tsgs[1])

        self.master.data["spawnchance"] = int(self.master.spawnchance_spin.get())
        if self.master.data["spawnchance"] == 0:
            self.master.data["spawnchance"] = False

        self.master.data["refreshrate"] = self.master.rfrsh_var.get()

        self.master.data["gridtype"] = self.master.gdt_var.get()

        self.master.data["outline"] = self.master.outline_var.get()

        self.master.data["rainbow"] = self.master.rainbow_var.get()
        
        self.master.delete_init()
        self.master.init_run()

        self.lmx = self.master.xsize*self.master.data["tilesize"]
        self.lmy = self.master.ysize*self.master.data["tilesize"]
        print("limits (in x y)", self.lmx, self.lmy)

        self.master.run()

    def handle_switch(self, event=False):
        if self.master.data["running"]:
            self.master.data["running"] = False
        else:
            self.master.data["running"] = True

    def handle_reset(self, event=False):
        self.master.data["running"] = False
        self.master.delete_run()
        self.master.start()

    def handle_m1pressed(self, event=False):
        self.master.m1pressed = True

    def handle_m1released(self, event=False):
        self.master.m1pressed = False

    def motion(self, event=False):
        if self.master.m1pressed:
            x, y = event.x, event.y
            if x < self.lmx and x > 0 and y < self.lmy and y > 0:
                #print("MOTION coords (x y)", x, y)
                self.master.to_draw.append((x, y))
                self.master.draw()
