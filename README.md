# InputDisplay

[Archived] : Will try again later or in another language  
PR and Suggestions are welcome tho

what does it do ?
- it show you your inputs (only keyboard for now)

fair warning : you'll need to run it as admin to have it work with some games  
Also, uses python 3.7 for now

more documentation WIP

todo :
 - add mouse events
 - try to handle caps lock?
 - make settings and all that BS
 - (OPTION) make it draw another window when the user click a button, to have a clean window without borders and all
 - handle caps_lock and scroll_lock to have a little "glow?" on them when active, see if it's doable to get their states somehow. also make all alphabet letters caps when caps_lock is active, if previous point is doable

foreseeable issues :
 - numpad. keys like numpad `-` will trigger the "regular" `-` key on the keyboard (right of `0` for ANSI layout). i can't seem to see a difference in "events" from `pynput`.
 - ISO enter key ... i have no idea how making a button for it would be handled.
 - mouse "extra" buttons, same issue as numpad. Especially if said buttons are binded to keys like `F1` for example
