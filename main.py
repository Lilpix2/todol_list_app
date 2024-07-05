from gui.gui import ToDoListGUI
import tkinter as tk

def main():
    root = tk.Tk()
    app = ToDoListGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
