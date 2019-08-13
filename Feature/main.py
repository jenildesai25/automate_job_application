import GUI
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    w = root.winfo_reqwidth()
    h = root.winfo_reqheight()
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('+%d+%d' % (x, y))
    my_gui = GUI.MyGUI(root)
    root.mainloop()
