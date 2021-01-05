from Source import main_window as mw,\
    input_events as ie,\
    draw_keyboard as dw,\
    draw_mouse as dm


if __name__ == '__main__':
    ie.kb_events()
    # ie.mouse_events()
    dw.make_keys()
    mw.root.mainloop()
