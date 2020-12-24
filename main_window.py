# import kivy.app
# import keyboard
import tkinter as tk
# import tkinter.ttk as ttk
import kb_layout

root = tk.Tk()
root.title("Virtual Keyboard")
root.attributes("-topmost", True)
# root.overrideredirect(1)    # Remove border
root.eval('tk::PlaceWindow . center')


for key in kb_layout.ANSI_TKL:
    print("x:" + str(key['Pos'][0]) + "-" + "y:" + str(key['Pos'][1]))
    tk.Button(root, text=key['Key']).grid(row=key['Pos'][0], column=['Pos'][1])
