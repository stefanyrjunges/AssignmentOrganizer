# AssignmentOrganizer.py
# @author Stefany R Junges
# 15/01/2024

import tkinter
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import os
import openpyxl 

def enter_data():
    assignment = assignment_entry.get()
    subject = subject_entry.get()
    duedate = duedate_entry.get()
    done = done_combobox.get()

    try:
        datetime.strptime(duedate, '%d/%m/%Y')
    except ValueError:
        messagebox.showwarning(message="Date format should be DD/MM/YYYY")
        return
    else:
        pass 
    
    if assignment == '' or subject == '' or duedate == '' or done == '':
        messagebox.showwarning(message="Please fill in all the forms")
    else:
        yesorno = messagebox.askyesno(message="Data saved. Would you like to add another assignment?")
    if yesorno:
        assignment_entry.delete(0, 'end')
        subject_entry.delete(0, 'end')
        duedate_entry.delete(0, 'end')
        done_combobox.delete(0, 'end')

    filepath = "ADD YOUR OWN FILEPATH HERE WITH THE NAME OF THE EXCEL FILE, WHETHER IT EXISTS OR NOT -> Example: C:\\Users\\....\\data.xlsx"

    if not os.path.exists(filepath):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        heading = ["Assignment name", "Module", "Due date", "Done?"]
        sheet.append(heading)
        sheet.append([assignment, subject, duedate, done])
        workbook.save(filepath)

    elif assignment != '' and subject != '' and duedate != '' and done != '':
        workbook = openpyxl.load_workbook(filepath)
        sheet = workbook.active
        sheet.append([assignment, subject, duedate, done])
        workbook.save(filepath)
    
    if yesorno == False:
        exit()

def cancel():
    cancel_message_box = messagebox.askyesno(message="Are you sure?")
    if cancel_message_box == True:
        exit()
    
def on_closing():
    if messagebox.askokcancel("Assignments Year X/Sem. Y", "Are you sure you want to quit?"):
        window.destroy()

window = tkinter.Tk() 
window.title("Assignments Year X/Sem. Y")
window.maxsize(415, 280)
window.config(bg="#d9d9d9")
window.geometry("415x280+550+200")

frame = tkinter.Frame(window)
frame.config(bg="#d9d9d9")
frame.pack()
user_info_frame = tkinter.LabelFrame(frame)
user_info_frame.config(bg="white", fg="#442c2e")
user_info_frame.grid(row= 1, column=0, padx=0, pady=10, ipady=5)

assignment_label = tkinter.Label(user_info_frame, text="Assignment name:")
assignment_label.grid(row=0, column=0, pady=5, padx=10)
assignment_label.config(bg="white", fg="#442c2e")

subject_label = tkinter.Label(user_info_frame, text="Module:")
subject_label.grid(row=1, column=0, pady=5, padx=10)
subject_label.config(bg="white", fg="#442c2e")

duedate_label = tkinter.Label(user_info_frame, text="Due date (DD/MM/YYYY):")
duedate_label.grid(row=2, column=0, pady=5, padx=10)
duedate_label.config(bg="white", fg="#442c2e")

done_label = tkinter.Label(user_info_frame, text="Done?")
done_label.grid(row=3, column=0, pady=5, padx=10)
done_label.config(bg="white", fg="#442c2e")

assignment_entry = tkinter.Entry(user_info_frame)
subject_entry = tkinter.Entry(user_info_frame)
duedate_entry = tkinter.Entry(user_info_frame)
done_combobox = ttk.Combobox(user_info_frame, values=["Yes", "No", "Partially"])

assignment_entry.grid(row=0, column=1, padx=10)
subject_entry.grid(row=1, column=1, padx=10)
duedate_entry.grid(row=2, column=1, padx=10)
done_combobox.grid (row=3, column=1, padx=10)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(sticky="ws")

stitle_frame = tkinter.LabelFrame(frame)
stitle_frame.grid(row=0, column=0, sticky="news")
stitle_frame.config(bg="#48798b")

title_label = tkinter.Label(stitle_frame, text="            Organize your assignments: quick and easy") 
title_label.grid(row=0, column=0, pady=20, padx=50, sticky="news")
title_label.config(bg="#48798b", fg="white")

button = tkinter.Button(frame, text="Submit", command= enter_data)
button.grid(row=2, column=0, padx=42, ipadx=30, sticky="w")
button.config(bg="white", fg="#442c2e")

buttonCancel = tkinter.Button(frame, text="Cancel", command= cancel)
buttonCancel.grid(row=2, column=0, padx=155, ipadx=30)
buttonCancel.config(bg="white", fg="#442c2e")

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()