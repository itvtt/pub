import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("도라에몽")
window.geometry("400x400")

canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

image = Image.open("doraemon.jpg")
doraemon_image = ImageTk.PhotoImage(image)


canvas.create_image(0, 0, image=doraemon_image, anchor='nw')

button = tk.Button(canvas, text="버튼")
button_window = canvas.create_window(150, 150, anchor='nw', window=button)

button_frame = tk.Frame(canvas)
button_frame_window = canvas.create_window(0, 0, anchor='nw', window=button_frame)

button1 = tk.Button(button_frame, text="버튼1")
button1.pack(side=tk.LEFT)
button2 = tk.Button(button_frame, text="버튼2")
button2.pack(side=tk.LEFT)

window.mainloop()
