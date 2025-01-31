import tkinter as tk
import time

def keep_running():
    
    while True:
        time.sleep(1)


root = tk.Tk()
root.title("ریدی داش بد بخت شدی")


label = tk.Label(root, text="")
label.pack(padx=10, pady=10)


keep_running()


root.mainloop()
