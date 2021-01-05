from pynput import keyboard, mouse
from Source import draw_keyboard as dw


def kb_on_press(key):
    dw.show_kb_press(key, sender='kb_press')


def kb_on_release(key):
    dw.show_kb_press(key, sender='kb_release')


def mouse_on_move(x, y):
    print(f"Mouse moved to ({x}, {y})")


def mouse_on_click(x, y, button, pressed):
    if pressed:
        print(f'Mouse clicked at ({x}, {y}) with {button}')


def mouse_on_scroll(x, y, dx, dy):
    print(f'Mouse scrolled at ({x}, {y})({dx}, {dy})')


def kb_events():
    kb_l = keyboard.Listener(on_press=kb_on_press, on_release=kb_on_release)
    kb_l.start()


def mouse_events():
    mouse_l = mouse.Listener(on_move=mouse_on_move, on_click=mouse_on_click, on_scroll=mouse_on_scroll)
    mouse_l.start()
