import tkinter as tk
import kb_layout
import main as m
import ctrl_combo as cc

root = tk.Tk()
root.title("InputDisplay")
root.attributes("-topmost", True)
# root.overrideredirect(1)    # Remove border
root.eval('tk::PlaceWindow . center')


def btn_txt(key):
    if key['Key'] == 'SPACER':
        return  # no text on a spacer, what's the point
    else:
        # This is just to make the text look nice
        if key['Key'].startswith('Key.'):
            text = key['Key'][len('Key.'):]
            # If there is an underscore
            if text.find('_') is not -1:
                # Just removing the not needed _l _r _gr
                if text.endswith('_l') or text.endswith('_r') or text.endswith('_gr'):
                    # This will need to be changed if there is a key that ends with _r _l _gr and needs a \n
                    # But i don't think there is?
                    return text.split('_', 1)[0].upper()
                else:
                    # Add a \n to make things look good
                    return text.replace('_', '\n').upper()
            else:
                # UPPERCASE
                return text.upper()
        else:
            # If it's just a regular key, just return it
            text = key['Key']
        return text


btn_list = []


def make_keys():
    # kb_layout.ANSI_TKL will need to change if adding more keyboard layouts
    for key in kb_layout.ANSI_TKL:
        # Handles the spacer to uhh, add spaces between the buttons so it looks like an actual keyboard
        if key['Key'] == 'SPACER':
            tk.Button(root, width=int(key['Size'][1] * 4), height=2, state='disabled', borderwidth=0)\
                .grid(row=key['Pos'][0], column=int(key['Pos'][1] * 4), columnspan=int(key['Size'][1] * 4),
                      sticky="NESW")
        else:   # aka if it's not a spacer
            # Here, the width and height are in text units? so we need to divide height by 2 to have a square
            btn = tk.Button(root, text=btn_txt(key), width=m.btn_size, height=int(m.btn_size/2), bg='grey')
            # sticky="NESW" is needed to have nicely aligned buttons
            btn.grid(row=key['Pos'][0], column=int(key['Pos'][1] * 4), columnspan=int(key['Size'][1] * 4),
                     sticky="NESW")
            if 'Shift' in key:
                btn_list.append({'Key': key['Key'], 'btn': btn, 'Shift': key['Shift']})
            else:
                btn_list.append({'Key': key['Key'], 'btn': btn})


def show_shift_keys(up):
    # This whole shit is to display shift keys when shift is pressed
    # kb_layout.ANSI_TKL will need to change if adding more keyboard layouts
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
            # handling that key press
            if repr(i['Key']) == repr(k):
                i['btn'].config(bg='red')
            # Handling if shift is held while pressing that key
            elif 'Shift' in i:
                if repr(i['Shift']) == repr(k):
                    i['btn'].config(bg='red')
            # Handling "Key.space" like keys press
            elif i['Key'] == str(k):
                i['btn'].config(bg='red')
            # Handling CTRL combo keys presses
            for j in cc.CTRL_COMBO:
                if repr(k) == repr(j['combo']) and repr(i['Key']) == repr(j['key']):
                    i['btn'].config(bg='red')
                elif repr(str(k)) == repr(str(j['combo'])) and repr(i['Key']) == repr(j['key']):
                    i['btn'].config(bg='red')
        # Changing the text on the keys that have a shift modifier
        if repr(str(k)) == repr('Key.shift') or repr(str(k)) == repr('Key.shift_r'):
            show_shift_keys(up='up')

    elif sender == 'kb_release':
        for i in btn_list:
            # Handling that key release
            if repr(i['Key']) == repr(k):
                i['btn'].config(bg='grey')
            # Handling shift with the release
            elif 'Shift' in i:
                if repr(i['Shift']) == repr(k):
                    i['btn'].config(bg='grey')
            # Handling "Key.space" like keys release
            elif i['Key'] == str(k):
                i['btn'].config(bg='grey')
            # Handling CTRL combo keys release
            for j in cc.CTRL_COMBO:
                if repr(k) == repr(j['combo']) and repr(i['Key']) == repr(j['key']):
                    i['btn'].config(bg='grey')
                elif repr(str(k)) == repr(str(j['combo'])) and repr(i['Key']) == repr(j['key']):
                    i['btn'].config(bg='grey')
        # Changing the text on the keys that have a shift modifier
        if repr(str(k)) == repr('Key.shift') or repr(str(k)) == repr('Key.shift_r'):
            show_shift_keys(up='down')
