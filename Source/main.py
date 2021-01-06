from Source import\
    main_window as mw,\
    input_events as ie,\
    draw_keyboard as dk,\
    draw_mouse as dm

if __name__ == '__main__':
    ie.kb_events()
    ie.mouse_events()
    dk.make_keys()
    dm.make_mouse()
    mw.root.mainloop()
