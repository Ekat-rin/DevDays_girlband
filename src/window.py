from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
from scipy.integrate import odeint
from tkinter.messagebox import *


color1='purple'
root = Tk() 
root.geometry("1300x710")
root['bg']=color1


frame1 = Frame(root,bg='indianRed4')
frame1.grid(row=1,column=1,columnspan=1)
listbox2 = OptionMenu(frame1, "режим" ,'1', '2', '3')
listbox2['bg']='lemon chiffon'
listbox2.grid(row=1,column=1,columnspan=1)

root.mainloop()
