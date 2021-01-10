from Source import\
    main_window as mw
import tkinter as tk
import time


# todo : handle mouse movement and scroll better


mouse_btn_list = []
mouse_move_btn_list = []
mouse_pos = [0, 0]


def make_mouse():
    mouse_frame = tk.Frame(mw.kb_m_frame, bd=5, relief='groove')
    mouse_frame.pack(side='right', fill='y')

    # Add all the buttons, simpler to do manually as it shouldn't need as modularity an the keyboard?
    left_btn = tk.Button(mouse_frame, bg='grey', width=mw.btn_size, height=int(mw.btn_size / 2))
    scroll_up_btn = tk.Button(mouse_frame, bg='grey', width=mw.btn_size, height=int(mw.btn_size / 2))
    middle_btn = tk.Button(mouse_frame, bg='grey', width=mw.btn_size, height=int(mw.btn_size / 2))
    scroll_down_btn = tk.Button(mouse_frame, bg='grey', width=mw.btn_size, height=int(mw.btn_size / 2))
    right_btn = tk.Button(mouse_frame, bg='grey', width=mw.btn_size, height=int(mw.btn_size / 2))
    # This one is a Frame
    mouse_movement_frame = tk.Frame(mouse_frame, width=mw.btn_size, height=int(mw.btn_size * 2))
    # Adding buttons for mouse movement
    mouse_move_up = tk.Button(mouse_movement_frame, bg='grey', width=mw.btn_size, height=int(mw.btn_size / 2))
    mouse_move_left = tk.Button(mouse_movement_frame, bg='grey', width=mw.btn_size, height=int(mw.btn_size / 2))
    mouse_move_right = tk.Button(mouse_movement_frame, bg='grey', width=mw.btn_size, height=int(mw.btn_size / 2))
    mouse_move_down = tk.Button(mouse_movement_frame, bg='grey', width=mw.btn_size, height=int(mw.btn_size / 2))

    # Grid all the buttons, doing them one by one is lame but ...
    left_btn.grid(row=0, rowspan=3, column=0, sticky="NESW")
    scroll_up_btn.grid(row=0, rowspan=1, column=1, sticky="NESW")
    middle_btn.grid(row=1, rowspan=1, column=1, sticky="NESW")
    scroll_down_btn.grid(row=2, rowspan=1, column=1, sticky="NESW")
    right_btn.grid(row=0, rowspan=3, column=2, sticky="NESW")
    # This one is a Frame!
    mouse_movement_frame.grid(row=3, column=0, columnspan=3, sticky="NESW", pady=(20, 0))
    # Grid the mouse_move btn
    mouse_move_up.grid(row=0, column=1, sticky='NESW')
    mouse_move_left.grid(row=1, column=0, sticky='NESW')
    mouse_move_right.grid(row=1, column=2, sticky='NESW')
    mouse_move_down.grid(row=2, column=1, sticky='NESW')

    # Append all the buttons to a list
    mouse_move_btn_list.append(mouse_move_up)
    mouse_move_btn_list.append(mouse_move_left)
    mouse_move_btn_list.append(mouse_move_right)
    mouse_move_btn_list.append(mouse_move_down)
    # Append all the buttons to a list to be able to change background color later
    mouse_btn_list.append(left_btn)
    mouse_btn_list.append(right_btn)
    mouse_btn_list.append(middle_btn)
    mouse_btn_list.append(scroll_up_btn)
    mouse_btn_list.append(scroll_down_btn)


def show_mouse_click(button, pressed):
    # Click pressed
    if pressed:
        # There might be a better way to do this ...
        if str(button) == 'Button.left':
            mouse_btn_list[0].config(bg='red')
        elif str(button) == 'Button.right':
            mouse_btn_list[1].config(bg='red')
        elif str(button) == 'Button.middle':
            mouse_btn_list[2].config(bg='red')
    # Click release
    elif not pressed:
        if str(button) == 'Button.left':
            mouse_btn_list[0].config(bg='grey')
        elif str(button) == 'Button.right':
            mouse_btn_list[1].config(bg='grey')
        elif str(button) == 'Button.middle':
            mouse_btn_list[2].config(bg='grey')


def show_mouse_scroll(dy):
    # dy == 1 is scroll "up"
    if dy == 1:
        mouse_btn_list[3].config(bg='red')
        # I can't think of a better solution for this
        # so it's a very short timer for now
        time.sleep(0.01)
        mouse_btn_list[3].config(bg='grey')
    # dy == -1 is scroll "down"
    elif dy == -1:
        mouse_btn_list[4].config(bg='red')
        time.sleep(0.01)
        mouse_btn_list[4].config(bg='grey')


def show_mouse_movement(x, y):
    # Main issue here is that the mouse position doesn't "update" when the mouse stop moving

    if x < mouse_pos[0]:
        mouse_move_btn_list[1].config(bg='red')
        time.sleep(0.001)
        mouse_move_btn_list[1].config(bg='grey')
    elif x > mouse_pos[0]:
        mouse_move_btn_list[2].config(bg='red')
        time.sleep(0.001)
        mouse_move_btn_list[2].config(bg='grey')

    if y < mouse_pos[1]:
        mouse_move_btn_list[0].config(bg='red')
        time.sleep(0.001)
        mouse_move_btn_list[0].config(bg='grey')
    elif y > mouse_pos[1]:
        mouse_move_btn_list[3].config(bg='red')
        time.sleep(0.001)
        mouse_move_btn_list[3].config(bg='grey')

    mouse_pos[0] = x
    mouse_pos[1] = y
