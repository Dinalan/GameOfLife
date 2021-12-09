import tkinter


WIN = tkinter.Tk()
WIN.title("Choose the version")
launch_GUI_options = ["2.x (pygame)", "1.x (tkinter)"]
user_launch_GUI_choice = tkinter.StringVar(WIN)
user_launch_GUI_choice.set(launch_GUI_options[0])

user_launch_GUI_menu = tkinter.OptionMenu(WIN, user_launch_GUI_choice, *launch_GUI_options)

user_launch_exp = tkinter.Label(WIN, text="Choose the version:      ")

def go(event=False):
    choice = user_launch_GUI_choice.get()
    WIN.destroy()
    if choice == "2.x (pygame)":
        print("pygame mode selected")
    if choice == "1.x (tkinter)":
        print("tkinter mode selected")
        from tkinterGUI.GUI import GUI
        gui = GUI()
        gui.start()



user_launch_GUI_button = tkinter.Button(WIN, text="GO!", command=go)

user_launch_exp.grid(row=1, column=0)
user_launch_GUI_menu.grid(row=1, column=1)
user_launch_GUI_button.grid(row=1, column=2)

if __name__ == '__main__':
    WIN.mainloop()
