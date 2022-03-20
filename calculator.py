from tkinter import *
root = Tk()
#to get the title name
root.title("CALCULATER")
#to get the background colour
root.config(bg = "#666666")

#to get the entry box to enter the expressions
value = StringVar(value = "Enter expression")
entry1 = Entry(root,textvariable = value, width = 35, borderwidth = 5)
entry1.grid(row = 0, column = 0, columnspan = 3, ipadx = 20,ipady = 10)


expression = ""


#to store the expression
def setexpression(num):
    global expression
    expression = expression + str(num)
    value.set(expression)

#to calculate the expression
def calculator():
    try:
        global expression
        answer = str(eval(expression))
        value.set(answer)
    except:
        value.set("enter correct expression")
        expression = ""

#to clear the expression
def clear():
    global expression
    expression = ""
    value.set(expression)
    
    
#defining the buttons
button_1 = Button(root, text = "1", padx = 40, pady = 20, command =lambda: setexpression("1"), fg = "blue", bg = "orange").grid(row = 3, column = 0)
button_2 = Button(root, text = "2", padx = 40, pady = 20, command =lambda: setexpression("2"), fg = "blue", bg = "orange").grid(row = 3, column = 1)
button_3 = Button(root, text = "3", padx = 40, pady = 20, command =lambda: setexpression("3"), fg = "blue", bg = "orange").grid(row = 3, column = 2)
button_4 = Button(root, text = "4", padx = 40, pady = 20, command =lambda: setexpression("4"), fg = "blue", bg = "orange").grid(row = 2, column = 0)
button_5 = Button(root, text = "5", padx = 40, pady = 20, command =lambda: setexpression("5"), fg = "blue", bg = "orange").grid(row = 2, column = 1)
button_6 = Button(root, text = "6", padx = 40, pady = 20, command =lambda: setexpression("6"), fg = "blue", bg = "orange").grid(row = 2, column = 2)
button_7 = Button(root, text = "7", padx = 40, pady = 20, command =lambda: setexpression("7"), fg = "blue", bg = "orange").grid(row = 1, column = 0)
button_8 = Button(root, text = "8", padx = 40, pady = 20, command =lambda: setexpression("8"), fg = "blue", bg = "orange").grid(row = 1, column = 1)
button_9 = Button(root, text = "9", padx = 40, pady = 20, command =lambda: setexpression("9"), fg = "blue", bg = "orange").grid(row = 1, column = 2)
button_0 = Button(root, text = "0", padx = 40, pady = 20, command =lambda: setexpression("0"), fg = "blue", bg = "orange").grid(row = 4, column = 1)
button_equal = Button(root, text = "=", padx = 40, pady = 20, command = calculator, fg = "white", bg = "green").grid(row = 6, column = 1, ipadx = 45, columnspan = 3)
button_clear = Button(root, text = "clear", padx = 30, pady = 20, command = clear,fg = "white", bg = "red").grid(row = 6, column = 0)
button_add = Button(root, text = "+", padx = 38, pady = 20, command =lambda: setexpression("+"),fg = "black", bg = "pink").grid(row = 4, column = 0)
button_sub = Button(root, text = "-", padx = 40, pady = 20, command =lambda: setexpression("-"),fg = "black", bg = "pink").grid(row = 5, column = 0)
button_mul = Button(root, text = "X", padx = 40, pady = 20, command =lambda: setexpression("*"),fg = "black", bg = "pink").grid(row = 5, column = 1)
button_div = Button(root, text = "/", padx = 40, pady = 20, command =lambda: setexpression("/"),fg = "black", bg = "pink").grid(row = 5, column = 2)
button_float = Button(root, text = ".", padx = 42, pady = 20, command =lambda: setexpression("."),fg = "black", bg = "pink").grid(row = 4, column = 2)

#displaying the buttons on the screen
'''button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_0.grid(row = 4, column = 1)
button_equal.grid(row = 6, column = 1, ipadx = 45, columnspan = 3)
button_add.grid(row = 4, column = 0)

button_clear.grid(row = 6, column = 0)
button_sub.grid(row = 5, column = 0)
button_mul.grid(row = 5, column = 1)

button_div.grid(row = 5, column = 2)
button_float.grid(row = 4, column = 2)'''

root.mainloop()
