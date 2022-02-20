#----------------------------------------GUI_MERGE-------------------------------------------------------

from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import os
from subprocess import call
import sys

#----------------------------------------FUNCTIONS-------------------------------------------------------

def system():
    call(["python", "system_check.py"])

def withmask():
    call(["python", "datapre.py"])

def test():
    call(["python", "test.py"])

def preprocess():
    call(["python", "social.py"])

def live():
    call(["python","main.py"])



root = Tk()
root.geometry('900x650')
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

bg = PhotoImage(file='E:\PROGRAMMING\PYTHON\CO-L-87\\1141.png')

my_canvas = Canvas(root, width=1000, height=750)
my_canvas.pack(fill='both', expand=True)

my_canvas.create_image(0,0,image = bg, anchor='nw')

my_canvas.create_text(475,70, text='CO_LIEUTANENT-87', font=('Fixedsys',52),fill='gray2')
#PaleGreen1
#CadetBlue3

#-------------------------------------BUTTONS------------------------------------------------------

btn1 = Button(root, text='SYSTEM_CHECK',height=5, width=60,font=('Fixedsys',16,BOLD))
btn2 = Button(root, text='DATA and PRE-PROCESSING',height=5, width=60,font=('Fixedsys',16,BOLD))
btn3 = Button(root, text='DETECT-FACE_MASK',height=5, width=60,font=('Fixedsys',16,BOLD))
btn4 = Button(root, text='SOCIAL-DISTACING',height=5, width=60,font=('Fixedsys',16,BOLD))
btn5 = Button(root, text='COVID-19 INFO',height=5, width=60,font=('Fixedsys',16,BOLD))

#-------------------------------------POSITION-------------------------------------------------------

btn1_window = my_canvas.create_window(210,130,anchor='nw', window= btn1)
btn2_window = my_canvas.create_window(210,230,anchor='nw', window= btn2)
btn3_window = my_canvas.create_window(210,330,anchor='nw', window= btn3)
btn4_window = my_canvas.create_window(210,430,anchor='nw', window= btn4)
btn5_window = my_canvas.create_window(210,530,anchor='nw', window= btn5)

#----------------------------------------WORKING-------------------------------------------------------

btn1.configure(command=system)
btn2.configure(command=withmask)
btn3.configure(command=test)
btn4.configure(command=preprocess)
btn5.configure(command=live)

#----------------------------------------STYLING-------------------------------------------------------

btn1.configure(activebackground="PaleGreen1")
btn2.configure(activebackground="PaleGreen1")
btn3.configure(activebackground="PaleGreen1")
btn4.configure(activebackground="PaleGreen1")
btn5.configure(activebackground="PaleGreen1")

btn1.configure(background="PaleGreen1")
btn2.configure(background="PaleGreen1")
btn3.configure(background="PaleGreen1")
btn4.configure(background="PaleGreen1")
btn5.configure(background="PaleGreen1")

btn1.configure(width=56)
btn2.configure(width=56)
btn3.configure(width=56)
btn4.configure(width=56)
btn5.configure(width=56)

btn1.configure(height=5)
btn2.configure(height=5)
btn3.configure(height=5)
btn4.configure(height=5)
btn5.configure(height=5)

btn1.configure(pady="1")
btn2.configure(pady="1")
btn3.configure(pady="1")
btn4.configure(pady="1")
btn5.configure(pady="1")

#----------------------------------------DETAILING-------------------------------------------------------

btn1.configure(foreground="#000000")
btn2.configure(foreground="#000000")
btn3.configure(foreground="#000000")
btn4.configure(foreground="#000000")
btn5.configure(foreground="#000000")

btn1.configure(highlightcolor="black")
btn2.configure(highlightcolor="black")
btn3.configure(highlightcolor="black")
btn4.configure(highlightcolor="black")
btn5.configure(highlightcolor="black")

btn1.configure(highlightbackground="greenyellow")
btn2.configure(highlightbackground="greenyellow")
btn3.configure(highlightbackground="greenyellow")
btn4.configure(highlightbackground="greenyellow")
btn5.configure(highlightbackground="greenyellow")

btn1.configure(activeforeground="#000000")
btn2.configure(activeforeground="#000000")
btn3.configure(activeforeground="#000000")
btn4.configure(activeforeground="#000000")
btn5.configure(activeforeground="#000000")

btn1.configure(disabledforeground="#bfbfbf")
btn2.configure(disabledforeground="#bfbfbf")
btn3.configure(disabledforeground="#bfbfbf")
btn4.configure(disabledforeground="#bfbfbf")
btn5.configure(disabledforeground="#bfbfbf")

my_canvas.configure(highlightbackground="red")

root.mainloop()
