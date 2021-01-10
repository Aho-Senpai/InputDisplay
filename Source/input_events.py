from pynput import\
    keyboard,\
    mouse
from Source import\
    draw_keyboard as dk,\
    draw_mouse as dm


def kb_on_press(key):
    dk.show_kb_press(key, sender='kb_press')


def kb_on_release(key):
    dk.show_kb_press(key, sender='kb_release')


def mouse_on_move(x, y):
    # dm.show_mouse_movement(x, y)
    return


def mouse_on_click(x, y, button, pressed):
    dm.show_mouse_click(button, pressed)


def mouse_on_scroll(x, y, dx, dy):
    dm.show_mouse_scroll(dy)


def kb_events():
    kb_l = keyboard.Listener(on_press=kb_on_press, on_release=kb_on_release)
    kb_l.start()


def mouse_events():
    mouse_l = mouse.Listener(on_move=mouse_on_move, on_click=mouse_on_click, on_scroll=mouse_on_scroll)
    mouse_l.start()
