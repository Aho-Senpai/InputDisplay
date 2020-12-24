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

one_u = '4'
one_25_u = '5'
one_5_u = '6'
one_75_u = '7'
two_u = '8'
two_25_u = '9'
two_75_u = '11'
six_25_u = '19'

for key in kb_layout.ANSI_TKL:
    if key['Size'] == '1U':
        tk.Button(root, text=key['Key'], width=one_u, height=one_u).grid(row=key['Pos'][0], column=key['Pos'][1])
    elif key['Size'] == '1.25U':
        tk.Button(root, text=key['Key'], width=one_25_u, height=one_u).grid(row=key['Pos'][0], column=key['Pos'][1])
    elif key['Size'] == '1.5U':
        tk.Button(root, text=key['Key'], width=one_5_u, height=one_u).grid(row=key['Pos'][0], column=key['Pos'][1])
    elif key['Size'] == '1.75U':
        tk.Button(root, text=key['Key'], width=one_75_u, height=one_u).grid(row=key['Pos'][0], column=key['Pos'][1])
    elif key['Size'] == '2U':
        tk.Button(root, text=key['Key'], width=two_u, height=one_u).grid(row=key['Pos'][0], column=key['Pos'][1])
    elif key['Size'] == '2.25U':
        tk.Button(root, text=key['Key'], width=two_25_u, height=one_u).grid(row=key['Pos'][0], column=key['Pos'][1])
    elif key['Size'] == '2.75U':
        tk.Button(root, text=key['Key'], width=two_75_u, height=one_u).grid(row=key['Pos'][0], column=key['Pos'][1])
    elif key['Size'] == '6.25U':
        tk.Button(root, text=key['Key'], width=six_25_u, height=one_u).grid(row=key['Pos'][0], column=key['Pos'][1])
