from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Food Securify")
root.geometry("800x600")  # Set initial size
root.configure(bg='white')

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def change_color(button, original_color):
    button.config(bg='blue')
    button.after(75, lambda: button.config(bg=original_color))

title_label = Label(root, text="Food Securify", font=("Times New Roman", 24, "bold"), bg='white')
title_label.pack(pady=20)

text_frame = Frame(root)
text_frame.pack(expand=True, fill=BOTH, padx=20)

scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=RIGHT, fill=Y)

text_box = Text(text_frame, height=15, font=("Arial", 12), bg='light blue', wrap=WORD, yscrollcommand=scrollbar.set)
scrollbar.config(command=text_box.yview)

text_box.insert(INSERT,
    "Hello, we are the Food Securify Team. Our names are Akshaj and Sourya, and we are from the IBT program in Lisgar Middle School.\n\n"
    "We have researched a variety of elements in food security and found some common reasons and data. Over 2 billion people faced moderate food insecurity and slightly less than 1 billion face severe food insecurity.\n\n"
    "Some reasons for Food Insecurity include:\n\n"
    "- High cost of living\n"
    "- Low income\n"
    "- Community factors\n"
    "- Health related factors\n"
    "- Unfairness to certain groups"
)

text_box.config(state="disabled")
text_box.pack(expand=True, fill=BOTH)

button_frame = Frame(root, bg='white')
button_frame.pack(pady=20)

btn1 = Button(button_frame, text="Places (Cheap Food)", width=20, bg='#97c0f7', command=lambda: change_color(btn1, '#97c0f7'))
btn2 = Button(button_frame, text="Cheap Dishes", width=20, bg='#72a1e5', command=lambda: change_color(btn2, '#72a1e5'))
btn3 = Button(button_frame, text="Calories Helper", width=20, bg='#4c82d3', command=lambda: change_color(btn3, '#4c82d3'))
btn4 = Button(button_frame, text="Water Tracker", width=20, bg='#1c64c1', command=lambda: change_color(btn4, '#1c64c1'))

btn1.pack(side=LEFT, padx=10)
btn2.pack(side=LEFT, padx=10)
btn3.pack(side=LEFT, padx=10)
btn4.pack(side=LEFT, padx=10)


center_window(root)

root.mainloop()
