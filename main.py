import input_events as ie
import main_window as mw


btn_size = 50


if __name__ == '__main__':
    ie.kb_events()
    # ie.mouse_events()
    mw.make_keys()
    # print(mw.btn_list)
    mw.root.mainloop()
