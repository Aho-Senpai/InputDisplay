import tkinter as tk

window = tk.Tk()
window.minsize(200, 200)

button = tk.Button(text="a")
button.pack()


def update_btn_alpha(key, sender):
    if (f'{key}' == 'Key.shift') and (sender == 'kb_press'):
        # Change a-z buttons to A-Z
        button['text'] = 'A'
    elif (f'{key}' == 'Key.shift') and (sender == 'kb_release'):
        # Change A-Z buttons to a-z
        button['text'] = 'a'

    if (f'{key}' == "'a'" or f'{key}' == "'A'") and sender == 'kb_press':
        button["bg"] = "red"
    elif (f'{key}' == "'a'" or f'{key}' == "'A'") and sender == 'kb_release':
        button['bg'] = "SystemButtonFace"
