import tkinter as tk


root = tk.Tk()
root.title("InputDisplay")
root.attributes("-topmost", True)
# root.overrideredirect(1)    # Remove border
root.eval('tk::PlaceWindow . center')

btn_size = 6
