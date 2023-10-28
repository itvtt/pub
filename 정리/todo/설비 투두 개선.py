import tkinter as tk
from tkinter import messagebox

def clear_selection():
    for var in group_vars.values():
            var.set(0)

def select_all_groups():
    if select_all_var.get() == 1:
        for var in group_vars.values():
            var.set(1)
        for group_key, var in group_vars.items():
            if var.get() == 1:
                add_task()  # 체크된 그룹에 대해 할 일 추가
    else:
        for var in group_vars.values():
            var.set(0)

def on_listbox_select(event):
    selected_listbox = event.widget
    selected_indices = selected_listbox.curselection()

    for listbox in listboxes.values():
        listbox.selection_clear(0, tk.END)  # Clear previous selections

    for index in selected_indices:
        selected_listbox.selection_set(index)  # Select clicked item

    update_delete_button_state()  # Update the state of the delete button

def load_tasks():
    for group_key, listbox in listboxes.items():
        listbox.delete(0, tk.END)  # Delete existing tasks in the listbox
        try:
            with open(f"{group_key}.txt", "r", encoding="utf-8") as file:  # Specify the correct file path
                tasks = file.readlines()
                for task in tasks:
                    listbox.insert(tk.END, task.strip())  # Add each task to the listbox
        except FileNotFoundError:
            pass


def get_selected_group2():
    selected_groups = [group_key for group_key, var in group_vars.items() if var.get()]
    if selected_groups:
        return selected_groups[0]  # Return the first selected group
    else:
        return None  # Return None if no group is selected
    

def get_selected_group():
    selected_groups = [group_key for group_key, listbox in listboxes.items() if listbox.curselection()]
    if selected_groups:
        return selected_groups[0]  # Return the first selected group
    else:
        return None  # Return None if no group is selected

def delete_task():
    selected_group_key = get_selected_group()

    if selected_group_key:
        selected_listbox = listboxes[selected_group_key]
        selected_indices = selected_listbox.curselection()

        if selected_indices:
            for index in selected_indices[::-1]:  # Reverse the indices to delete from the end first
                selected_listbox.delete(index)
            messagebox.showinfo("Notification", "Task(s) deleted.")
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")
    else:
        messagebox.showwarning("Warning", "Please select a group.")

    update_delete_button_state()  # Update the state of the delete button

def add_task():
    task = entry.get()
    selected_groups = [group_key for group_key, var in group_vars.items() if var.get()]

    if task and selected_groups:
        for group_key in selected_groups:
            group_title = group_dict[group_key]
            task_with_group = f"{group_title} - {task}"
            current_listbox = listboxes[group_key]
            current_listbox.insert(tk.END, task_with_group)
        entry.delete(0, tk.END)
        
def save_tasks():
    for group_key, listbox in listboxes.items():
        tasks = listbox.get(0, tk.END)
        filename = f"{group_key}.txt"

        with open(filename, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(f"{task}\n")

    messagebox.showinfo("Notification", "Tasks saved.")

def update_delete_button_state():
    selected_group_key = get_selected_group()

    if selected_group_key:
        selected_listbox = listboxes[selected_group_key]
        selected_indices = selected_listbox.curselection()

        if selected_indices:
            delete_button.config(state=tk.NORMAL)  # Enable the delete button
        else:
            delete_button.config(state=tk.DISABLED)  # Disable the delete button
    else:
        delete_button.config(state=tk.DISABLED)  # Disable the delete button

root = tk.Tk()
root.title("Todo List")

# Group information
group_dict = {
    "Group 1": "Group 1",
    "Group 2": "Group 2",
    "Group 3": "Group 3",
    "Group 4": "Group 4",
    "Group 5": "Group 5",
    "Group 6": "Group 6",
    "Group 7": "Group 7",
    "Group 8": "Group 8",
    "Group 9": "Group 9",
    "Group 10": "Group 10",
    "Group 11": "Group 11",
    "Group 12": "Group 12",
    "Group 13": "Group 13",
    "Group 14": "Group 14",
    "Group 15": "Group 15",
    "Group 16": "Group 16",
    "Group 17": "Group 17",
    "Group 18": "Group 18",
    "Group 19": "Group 19",
    "Group 20": "Group 20",
    "Group 21": "Group 21",
    "Group 22": "Group 22",
    "Group 23": "Group 23",
    "Group 24": "Group 24"
}


# 그룹 선택 체크 박스
group_frame = tk.Frame(root)
group_frame.pack(pady=10)

# 그룹 체크 박스 배치
select_all_var = tk.IntVar()
select_all_check = tk.Checkbutton(group_frame, text="전체 선택", variable=select_all_var, onvalue=1, offvalue=0,
                                  command=select_all_groups)
select_all_check.grid(row=0, column=0, padx=5)

group_vars = {}
row_count = 1  # row_count를 1로 초기화
column_count = 0
for group_key, group_title in group_dict.items():
    var = tk.IntVar()
    group_check = tk.Checkbutton(group_frame, text=group_title, variable=var, onvalue=1, offvalue=0, width=10)
    group_check.grid(row=row_count, column=column_count, padx=5, pady=5)
    group_vars[group_key] = var

    column_count += 1
    if column_count >= 12:
        row_count += 1
        column_count = 0

clear_selection_button = tk.Checkbutton(group_frame, text="체크 해제", command=clear_selection)
clear_selection_button.grid(row=0, column=1, padx=5)


# Listbox frame
listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10)

# Listboxes
listboxes = {}
row_count = 0
column_count = 0
for group_key, group_title in group_dict.items():
    listbox = tk.Listbox(listbox_frame, width=40, height=10, selectbackground="light blue", selectmode=tk.MULTIPLE)
    listbox.grid(row=row_count, column=column_count, padx=5, pady=5)
    title_label = tk.Label(listbox_frame, text=group_title)
    title_label.grid(row=row_count, column=column_count, padx=5, pady=5)
    listbox.bind("<<ListboxSelect>>", on_listbox_select)
    listboxes[group_key] = listbox

    column_count += 1
    if column_count >= 6:
        row_count += 1
        column_count = 0

# Scrollbar
scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.grid(row=row_count, column=column_count, sticky="NS")

for listbox in listboxes.values():
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)




# Task entry
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, font=("Helvetica", 12))
entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add", command=add_task)
add_button.grid(row=0, column=0, padx=10)

delete_button = tk.Button(button_frame, text="Delete", command=delete_task, state=tk.DISABLED)
delete_button.grid(row=0, column=1, padx=10)

save_button = tk.Button(button_frame, text="Save", command=save_tasks)
save_button.grid(row=0, column=2, padx=10)

# Load tasks
load_tasks()

root.mainloop()
