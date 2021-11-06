import tkinter as tk
from tkinter.font import Font

root = tk.Tk()
root.title("Birthday Card")
root.option_add('*Font', '10')
root.geometry('750x300')
root.configure(bg="#ffecad")

text = tk.Label(bg = "#ffecad", text="Happy birthday Dad!")
text.pack()
def moreText(*args):
    
    line1 = tk.Label(bg = "#ffecad", text = "I know this isn't much for a present, but I'm still learning tkinter so I hope this is ok.")  
    line2 = tk.Label(bg = "#ffecad", text = "Anyways, happy birthday and thank you for pushing me into learning to code! ")
    line3 = tk.Label(bg = "#ffecad", text = "You truly are a great dad!")
    line1.pack()
    line2.pack()
    line3.pack()
    button.destroy()
button = tk.Button(bg = "#d9adff",text = "Click for more!", command=moreText)
button.pack()
root.mainloop()