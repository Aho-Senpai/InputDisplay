# import keyboard
import tkinter as tk
# import tkinter.ttk as ttk
import kb_layout
import main as m

root = tk.Tk()
root.title("InputDisplay")
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
    for key in kb_layout.ANSI_TKL:
        if key['Key'] == 'SPACER':
            tk.Button(root, width=int(key['Size'][1] * 4), height=2, state='disabled', borderwidth=0)\
                .grid(row=key['Pos'][0], column=int(key['Pos'][1] * 4), columnspan=int(key['Size'][1] * 4),
                      sticky="NESW")
        else:
            btn = tk.Button(root, text=btn_txt(key), width=m.btn_size, height=int(m.btn_size/2), bg='grey',
                            compound='c')
            btn.grid(row=key['Pos'][0], column=int(key['Pos'][1] * 4), columnspan=int(key['Size'][1] * 4),
                     sticky="NESW")
            btn_list.append({'Key': key['Key'], 'btn': btn})


def show_shift_keys(up):
    for i in kb_layout.ANSI_TKL:
        if 'Shift' in i:
            for j in btn_list:
                if repr(j['Key']) == repr(i['Key']):
                    if up == 'up':
                        j['btn'].config(text=i['Shift'])
                    elif up == 'down':
                        j['btn'].config(text=btn_txt(i))


def show_kb_press(k, sender):
    if sender == 'kb_press':
        for i in btn_list:
            if repr(i['Key']) == repr(k):
                i['btn'].config(bg='red')
            elif i['Key'] == str(k):
                i['btn'].config(bg='red')
        if repr(str(k)) == repr('Key.shift') or repr(str(k)) == repr('Key.shift_r'):
            show_shift_keys(up='up')

    elif sender == 'kb_release':
        for i in btn_list:
            if repr(i['Key']) == repr(k):
                i['btn'].config(bg='grey')
            elif i['Key'] == str(k):
                i['btn'].config(bg='grey')
        if repr(str(k)) == repr('Key.shift') or repr(str(k)) == repr('Key.shift_r'):
            show_shift_keys(up='down')
