import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("도라에몽")
window.geometry("400x400")

canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

image = Image.open("doraemon.jpg")
doraemon_image = ImageTk.PhotoImage(image)

button = tk.Button(canvas, text="버튼", image=doraemon_image, compound=tk.CENTER)
button_window = canvas.create_window(150, 150, anchor='nw', window=button)

button_frame = tk.Frame(canvas)
button_frame_window = canvas.create_window(0, 0, anchor='nw', window=button_frame)

image1 = Image.open("button1.png")
button_image1 = ImageTk.PhotoImage(image1)
button1 = tk.Button(button_frame, image=button_image1)
button1.pack(side=tk.LEFT)

image2 = Image.open("button2.png")
button_image2 = ImageTk.PhotoImage(image2)
button2 = tk.Button(button_frame, image=button_image2)
button2.pack(side=tk.LEFT)

window.mainloop()
