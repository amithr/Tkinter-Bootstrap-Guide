import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")

def open_dialog_1():
    app = ttk.Toplevel(title="My Toplevel")
    app.mainloop()


open_button = ttk.Button(root, text="Open", command=open_dialog, bootstyle=SUCCESS)
open_button.pack(side=LEFT, padx=5, pady=10)

exit_button = ttk.Button(root, text="Exit", bootstyle=(INFO, OUTLINE))
exit_button.pack(side=LEFT, padx=5, pady=10)

root.mainloop()