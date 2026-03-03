import tkinter as tk

root = tk.Tk()

function = []
number1 = []
number2 = []

def c1():
    print("1", end = "")
    function.append('1')

def c2():
    print("2", end = "")
    function.append('2')

def c3():
    print("3", end = "")
    function.append('3')

def c4():
    print("4", end = "")
    function.append('4')

def c5():
    print("5", end = "")
    function.append('5')

def c6():
    print("6", end = "")
    function.append('6')

def c7():
    print("7", end = "")
    function.append('7')

def c8():
    print("8", end = "")
    function.append('8')

def c9():
    print("9", end = "")
    function.append('9')

def plus():
    print (" + ", end = "")
    function.append("+")

def equals():
    print (f' = {eval(''.join(function))}')
    print 
    

button1 = tk.Button(root, text = "  1  ", command = c1)
button2 = tk.Button(root, text = "  2  ", command = c2)
button3 = tk.Button(root, text = "  3  ", command = c3)
plus = tk.Button(root, text = "  +  ", command = plus)
button1.grid(row = 0, column = 0)
button2.grid(row = 0, column = 1)
button3.grid(row = 0, column = 2)
plus.grid(row = 0, column = 3)

button4 = tk.Button(root, text = "  4  ", command = c4)
button5 = tk.Button(root, text = "  5  ", command = c5)
button6 = tk.Button(root, text = "  6  ", command = c6)
minus = tk.Button(root, text = "  -  ", command = plus)
button4.grid(row = 1, column = 0)
button5.grid(row = 1, column = 1)
button6.grid(row = 1, column = 2)
minus.grid(row = 1, column = 3)

button7 = tk.Button(root, text = "  7  ", command = c7)
button8 = tk.Button(root, text = "  8  ", command = c8)
button9 = tk.Button(root, text = "  9  ", command = c9)
equals = tk.Button(root, text = "  =  ", command = equals)
button7.grid(row = 2, column = 0)
button8.grid(row = 2, column = 1)
button9.grid(row = 2, column = 2)
equals.grid(row = 2, column = 3)

root.mainloop()
