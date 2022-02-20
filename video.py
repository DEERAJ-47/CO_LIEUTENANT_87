from tkinter import*
import random
import os
from tkinter import ttk
from tkinter.font import BOLD
import os
from subprocess import call
import sys

def VHS1():
       filename = 'predict_video.py'
       os.system(filename)
       os.system('notepad'+filename)

def VHS2():
       filename = 'predict_video1.py'
       os.system(filename)
       os.system('notepad'+filename)

def VHS3():
       filename = 'predict_video2.py'
       os.system(filename)
       os.system('notepad'+filename)

def VHS4():
       filename = 'predict_video3.py'
       os.system(filename)
       os.system('notepad'+filename)


root = Tk()
root.geometry('900x550')
root.title("CO_LIEUTANENT-87")


#----------------------------------------PRE-DEFINITION-------------------------------------------------------
'''This class configures and populates the toplevel window.
    top is the toplevel containing window.'''
bgcolor = 'greenyellow'  # X11 color: 'gray85'
fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#ffffff' # X11 color: 'white'
_ana1color = '#ffffff' # X11 color: 'white'
_ana2color = '#ffffff' # X11 color: 'white'
        
font14 = "-family {Fixedsys} -size 18 -weight bold -slant "  \
"roman -underline 0 -overstrike 0"
font16 = "-family {Fixedsys} -size 44 -weight bold "  \
"-slant roman -underline 0 -overstrike 0"
font9 = "-family {Fixedsys} -size 9 -weight normal -slant "  \
"roman -underline 0 -overstrike 0"

#----------------------------------------IMAGE-------------------------------------------------------

bg = PhotoImage(file='E:\PROGRAMMING\PYTHON\CO-L-87\\1131.png')

my_canvas = Canvas(root, width=1000, height=850)
my_canvas.pack(fill='both', expand=True)

my_canvas.create_image(0,0,image = bg, anchor='nw')

my_canvas.create_text(475,70, text='VHS-LIST', font=('Fixedsys',52),fill='black')
#PaleGreen1
#CadetBlue3

#-------------------------------------BUTTONS------------------------------------------------------

btn1 = Button(root, text='VHS-1',height=5, width=60,font=('Fixedsys',16,BOLD))
btn2 = Button(root, text='VHS-2',height=5, width=60,font=('Fixedsys',16,BOLD))
btn3 = Button(root, text='VHS-3',height=5, width=60,font=('Fixedsys',16,BOLD))
btn4 = Button(root, text='VHS-4',height=5, width=60,font=('Fixedsys',16,BOLD))
#btn5 = Button(root, text='VHS-5',height=5, width=60,font=('Fixedsys',16,BOLD))
#btn6 = Button(root, text='VHS-6',height=5, width=60,font=('Fixedsys',16,BOLD))
#btn7 = Button(root, text='VHS-7',height=5, width=60,font=('Fixedsys',16,BOLD))

#-------------------------------------POSITION-------------------------------------------------------

btn1_window = my_canvas.create_window(210,130,anchor='nw', window= btn1)
btn2_window = my_canvas.create_window(210,215,anchor='nw', window= btn2)
btn3_window = my_canvas.create_window(210,300,anchor='nw', window= btn3)
btn4_window = my_canvas.create_window(210,385,anchor='nw', window= btn4)
#btn5_window = my_canvas.create_window(210,470,anchor='nw', window= #btn5)
#btn6_window = my_canvas.create_window(210,555,anchor='nw', window= #btn6)
#btn6_window = my_canvas.create_window(210,638,anchor='nw', window= #btn7)

#----------------------------------------WORKING-------------------------------------------------------

btn1.configure(command=VHS1)
btn2.configure(command=VHS2)
btn3.configure(command=VHS3)
btn4.configure(command=VHS4)
#btn5.configure(command=VHS5)
#btn5.configure(command=VHS6)
#btn5.configure(command=VHS7)

#----------------------------------------STYLING-------------------------------------------------------

btn1.configure(activebackground="Steel Blue1")
btn2.configure(activebackground="Steel Blue1")
btn3.configure(activebackground="Steel Blue1")
btn4.configure(activebackground="Steel Blue1")
#btn5.configure(activebackground="Steel Blue1")
#btn6.configure(activebackground="Steel Blue1")
#btn6.configure(activebackground="Steel Blue1")

btn1.configure(background="Steel Blue1")
btn2.configure(background="Steel Blue1")
btn3.configure(background="Steel Blue1")
btn4.configure(background="Steel Blue1")
#btn5.configure(background="Steel Blue1")
#btn6.configure(background="Steel Blue1")
#btn7.configure(background="Steel Blue1")

btn1.configure(width=56)
btn2.configure(width=56)
btn3.configure(width=56)
btn4.configure(width=56)
#btn5.configure(width=56)
#btn6.configure(width=56)
#btn7.configure(width=56)

btn1.configure(height=3)
btn2.configure(height=3)
btn3.configure(height=3)
btn4.configure(height=3)
#btn5.configure(height=3)
#btn6.configure(height=3)
#btn7.configure(height=3)

btn1.configure(pady="1")
btn2.configure(pady="1")
btn3.configure(pady="1")
btn4.configure(pady="1")
#btn5.configure(pady="1")
#btn6.configure(pady="1")
#btn7.configure(pady="1")

#----------------------------------------DETAILING-------------------------------------------------------

btn1.configure(foreground="#000000")
btn2.configure(foreground="#000000")
btn3.configure(foreground="#000000")
btn4.configure(foreground="#000000")
#btn5.configure(foreground="#000000")
#btn6.configure(foreground="#000000")
#btn7.configure(foreground="#000000")

btn1.configure(highlightcolor="black")
btn2.configure(highlightcolor="black")
btn3.configure(highlightcolor="black")
btn4.configure(highlightcolor="black")
#btn5.configure(highlightcolor="black")
#btn6.configure(highlightcolor="black")
#btn7.configure(highlightcolor="black")

btn1.configure(highlightbackground="greenyellow")
btn2.configure(highlightbackground="greenyellow")
btn3.configure(highlightbackground="greenyellow")
btn4.configure(highlightbackground="greenyellow")
#btn5.configure(highlightbackground="greenyellow")
#btn6.configure(highlightbackground="greenyellow")
#btn7.configure(highlightbackground="greenyellow")

btn1.configure(activeforeground="#000000")
btn2.configure(activeforeground="#000000")
btn3.configure(activeforeground="#000000")
btn4.configure(activeforeground="#000000")
#btn5.configure(activeforeground="#000000")
#btn6.configure(activeforeground="#000000")
#btn7.configure(activeforeground="#000000")

btn1.configure(disabledforeground="#bfbfbf")
btn2.configure(disabledforeground="#bfbfbf")
btn3.configure(disabledforeground="#bfbfbf")
btn4.configure(disabledforeground="#bfbfbf")
#btn5.configure(disabledforeground="#bfbfbf")
#btn6.configure(disabledforeground="#bfbfbf")
#btn7.configure(disabledforeground="#bfbfbf")

my_canvas.configure(highlightbackground="red")

root.mainloop()
