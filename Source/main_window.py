import tkinter as tk


root = tk.Tk()
root.title("InputDisplay")
root.attributes("-topmost", True)
# root.overrideredirect(1)    # Remove border
root.eval('tk::PlaceWindow . center')

kb_m_frame = tk.Frame(root)
kb_m_frame.pack(side='bottom')

btn_size = 6
