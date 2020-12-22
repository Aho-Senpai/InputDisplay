from pynput import keyboard, mouse
import main_window


def kb_on_press(key):
    print(f"{key} pressed")
    # main_window.button["text"] = f"{key}" # This works, commented for latter reference.
    main_window.update_btn_alpha(key, sender='kb_press')


def kb_on_release(key):
    print(f"{key} released")
    main_window.update_btn_alpha(key, sender='kb_release')


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