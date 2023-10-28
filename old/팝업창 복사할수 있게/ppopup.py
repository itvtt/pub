import tkinter as tk

def create_popup(text):
    root = tk.Tk()
    root.withdraw()

    popup = tk.Toplevel(root)
    popup.title("팝업 창")
    popup.geometry("500x400")

    text_box = tk.Text(popup, height=60, width=100)
    text_box.insert(tk.END, text)
    text_box.pack()

    popup.mainloop()

text = "안녕하세요! 이것은 큰 크기의 텍스트 팝업 창입니다."
create_popup(text)
