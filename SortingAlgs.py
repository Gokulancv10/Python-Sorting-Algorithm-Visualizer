import tkinter
from tkinter import *
from tkinter import ttk
import random
import time
from BubbleSort import bubble_sort_alg
from quicksortalg import quick_sort


root = Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(900, 600)
root.config(bg = 'black')

# VARIABLES
selected_alg = StringVar()

# global data which is selected on sliding bar
data = []

def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    
    normalizedData = [i/ max(data) for i in data]

    for i, height in enumerate(normalizedData):
        # top left
        x0 = i* x_width + offset + spacing
        y0 = c_height - height* 340
        # bottom right
        x1 = (i+1) * x_width + offset
        y1 = c_height
        
        # BAR CHART
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()

def Generate():
    global data
    
    # print("ALg Selected: " + selected_alg.get())
    
    minVal = int(MinEntry.get())
    maxVal = int(MaxEntry.get())
    size = int(sizeEntry.get())

    
    data = []
    for _ in range(size):
        data .append(random.randrange(minVal, maxVal+1))
    drawData(data, ['red' for x in range(len(data))])


def StartAlgorithm():
    global data
    if not data:
        return
    
    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
        drawData(data, ['green' for x in range(len(data))])
        
    elif algMenu.get() == 'Bubble Sort':  
        bubble_sort_alg(data, drawData, speedScale.get())
    

# frame / base layout
UI_frame = Frame(root, width = 600, height = 200, bg = 'grey')
UI_frame.grid(row = 0, column = 0, padx = 10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# USER INTERFACE AREA
# row[0]
Label(UI_frame, text='Algorithm', bg='grey', fg='white').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Quick Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=int(0.1), to=int(2.0), length=200, digits=int(0.2), resolution=int(0.2), orient=HORIZONTAL, label='Select Speed [s]',bg='white',fg='blue')
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm,bg='red').grid(row=0, column=3, padx=5, pady=5)



# ROW[1]
# Label(UI_frame, text='Size', bg='grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1,
                  orient=HORIZONTAL, label='Data Size', bg='white', fg='blue')
sizeEntry.grid(row=1, column=0, padx=5, pady=5)


# Label(UI_frame, text='Min Value', bg='grey').grid(row=1, column=2, padx=5, pady=5, sticky=W)
MinEntry = Scale(UI_frame, from_=1, to=10, resolution=1,
                 orient=HORIZONTAL, label='Min Value', bg='white', fg='blue')
MinEntry.grid(row=1, column=1, padx=5, pady=5)

# Label(UI_frame, text='Max Value', bg='grey').grid(
    # row=1, column=4, padx=5, pady=5, sticky=W)
MaxEntry = Scale(UI_frame, from_=10, to=100,  resolution=1,
                 orient=HORIZONTAL, label='Max Value', bg='white', fg='blue')
MaxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
