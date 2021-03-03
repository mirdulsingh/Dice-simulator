
import tkinter
import random

# toplevel widget of Tk which represents mostly the main window of an application
root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll Dice')

# label to display dice
label = tkinter.Label(root, text='', font=('Helvetica', 260))


# function part
def roll_dice():
    # unicode character strings for dice(U+2683-------> \u2680)
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text={random.choice(dice)})
    label.pack()

# button
button = tkinter.Button(root, text='roll dice', foreground='green', command=roll_dice)
button.pack()

root.mainloop()