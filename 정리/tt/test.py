import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("안내", "안녕하세요!")

# 메인 창 생성
root = tk.Tk()
root.title("버튼 예제")

# 버튼 생성
button = tk.Button(root, text="클릭하세요", command=show_message)

# 버튼 배치
button.pack(pady=20)

# 이벤트 루프 시작
root.mainloop()
