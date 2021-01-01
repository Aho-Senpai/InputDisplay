# import keyboard
import tkinter as tk
# import tkinter.ttk as ttk
import kb_layout

root = tk.Tk()
root.title("Virtual Keyboard")
root.attributes("-topmost", True)
# root.overrideredirect(1)    # Remove border
root.eval('tk::PlaceWindow . center')


def btn_txt(key):
    if key['Key'] == 'SPACER':
        return 'AAA'
    else:
        text = key['Key']
        return text


def make_keys():
    for key in kb_layout.ANSI_TKL:
        if key['Key'] == 'SPACER':
            tk.Button(root, width=int(key['Size'][1] * 4), height=2, state='disabled', borderwidth=0)\
                .grid(row=key['Pos'][0], column=int(key['Pos'][1] * 4), columnspan=int(key['Size'][1] * 4),
                      sticky="NESW")
        else:
            tk.Button(root, text=btn_txt(key), width=int(key['Size'][1] * 4), height=2, bg='grey')\
                .grid(row=key['Pos'][0], column=int(key['Pos'][1] * 4), columnspan=int(key['Size'][1] * 4),
                      sticky="NESW")


def show_kb_press(k, sender):
    if sender == 'kb_press':
        print(str(k) + ' press')

#     elif sender == 'kb_release':
# print('release')
