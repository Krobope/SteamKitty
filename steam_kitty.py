import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("SteamKitty")
root.iconbitmap("icon.ico")

img = Image.open("wavingcat.png")
photo = ImageTk.PhotoImage(img)
label = tk.Label(root, image=photo)
label.pack()

root.attributes("-toolwindow", True)
root.attributes("-topmost", False)
root.after(5000, root.iconify)
root.mainloop()
