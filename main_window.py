# import keyboard
import tkinter as tk
# import tkinter.ttk as ttk
import kb_layout
import main as m

root = tk.Tk()
root.title("Virtual Keyboard")
root.attributes("-topmost", True)
# root.overrideredirect(1)    # Remove border
root.eval('tk::PlaceWindow . center')


def btn_txt(key):
    if key['Key'] == 'SPACER':
        return
    else:
        # This is just to make the text look nice
        if key['Key'].startswith('Key.'):
            text = key['Key'][len('Key.'):]
            if text.find('_') is not -1:
                if text.endswith('_l') or text.endswith('_r') or text.endswith('_gr'):
                    return text.split('_', 1)[0].upper()
                else:
                    return text.replace('_', '\n').upper()
            else:
                return text.upper()
        else:
            text = key['Key']
        return text


btn_list = []


def make_keys():
    image = tk.PhotoImage(width=1, height=1)
    for key in kb_layout.ANSI_TKL:
        if key['Key'] == 'SPACER':
            tk.Button(root, width=int(key['Size'][1] * 4), height=2, state='disabled', borderwidth=0)\
                .grid(row=key['Pos'][0], column=int(key['Pos'][1] * 4), columnspan=int(key['Size'][1] * 4),
                      sticky="NESW")
        else:
            btn = tk.Button(root, text=btn_txt(key), width=m.btn_size, height=m.btn_size, bg='grey', image=image,
                            compound='c')
            btn.grid(row=key['Pos'][0], column=int(key['Pos'][1] * 4), columnspan=int(key['Size'][1] * 4),
                     sticky="NESW")
            btn_list.append({'Key': key['Key'], 'btn': btn})


def show_kb_press(k, sender):
    if sender == 'kb_press':
        print(k)
        for i in btn_list:
            if repr(i['Key']) == repr(k):
                i['btn'].config(bg='red')
            elif i['Key'] == str(k):
                i['btn'].config(bg='red')

#    elif sender == 'kb_release':
#        print('release')
