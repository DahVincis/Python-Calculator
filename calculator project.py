import tkinter


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


cal = tkinter.Tk()
cal.title("Calculator")
operator = ""
text_Input = tkinter.StringVar()

txtDisplay = tkinter.Entry(cal, font=('Times', 25, 'bold'), fg="Light Gray", textvariable=text_Input, bd=20, insertwidth=5,
                           bg="dark slate gray", justify='right').grid(columnspan=4)

btn7 = tkinter.Button(cal, padx=12, pady=12, bd=5, fg="black", font=('arial', 30, 'bold'),
                      text="7", bg="slate gray", command=lambda: btnClick(7)).grid(row=1, column=0)
btn8 = tkinter.Button(cal, padx=12, pady=12, bd=5, fg="black", font=('arial', 30, 'bold'),
                      text="8", bg="slate gray", command=lambda: btnClick(8)).grid(row=1, column=1)
btn9 = tkinter.Button(cal, padx=12, pady=12, bd=5, fg="black", font=('arial', 30, 'bold'),
                      text="9", bg="slate gray", command=lambda: btnClick(9)).grid(row=1, column=2)
Addition = tkinter.Button(cal, padx=12, pady=12, bd=5, fg="black", font=('arial', 30),
                          text="+", bg="dark red", command=lambda: btnClick("+")).grid(row=1, column=3)
# ==========================================================================================
btn4 = tkinter.Button(cal, padx=12, pady=12, bd=5, fg="black", font=('arial', 30, 'bold'),
                      text="4", bg="slate gray", command=lambda: btnClick(4)).grid(row=2, column=0)
btn5 = tkinter.Button(cal, padx=12, pady=12, bd=5, fg="black", font=('arial', 30, 'bold'),
                      text="5", bg="slate gray", command=lambda: btnClick(5)).grid(row=2, column=1)
btn6 = tkinter.Button(cal, padx=12, pady=12, bd=5, fg="black", font=('arial', 30, 'bold'),
                      text="6", bg="slate gray", command=lambda: btnClick(6)).grid(row=2, column=2)
Subtraction = tkinter.Button(cal, padx=12, pady=12, bd=5, fg="black", font=('arial', 30),
                             text="-", bg="dark red", command=lambda: btnClick("-")).grid(row=2, column=3)
# ==========================================================================================
btn1 = tkinter.Button(cal, padx=12, pady=12, bd=5, fg="black", font=('arial', 30, 'bold'),
                      text="1", bg="slate gray", command=lambda: btnClick(1)).grid(row=3, column=0)
btn2 = tkinter.Button(cal, padx=12, pady=12, bd=5, fg="black", font=('arial', 30, 'bold'),
                      text="2", bg="slate gray", command=lambda: btnClick(2)).grid(row=3, column=1)
btn3 = tkinter.Button(cal, padx=12, pady=12, bd=5, fg="black", font=('arial', 30, 'bold'),
                      text="3", bg="slate gray", command=lambda: btnClick(3)).grid(row=3, column=2)
Multiply = tkinter.Button(cal, padx=12, pady=12, bd=5, fg="black", font=('arial', 30),
                          text="*", bg="dark red", command=lambda: btnClick("*")).grid(row=3, column=3)
# ==========================================================================================
btn0 = tkinter.Button(cal, padx=12, pady=12, bd=5, fg="black", font=('arial', 30, 'bold'),
                      text="0", bg="slate gray", command=lambda: btnClick(0)).grid(row=4, column=0)
btnClear = tkinter.Button(cal, padx=12, pady=12, bd=5, fg="black", font=('arial', 30),
                          text="C", bg="slate gray", command=btnClearDisplay).grid(row=4, column=1)
btnEquals = tkinter.Button(cal, padx=12, pady=12, bd=5, fg="black", font=('arial', 30),
                           text="=", bg="slate gray", command=btnEqualsInput).grid(row=4, column=2)
Division = tkinter.Button(cal, padx=12, pady=12, bd=5, fg="black", font=('arial', 30),
                          text="/", bg="dark red", command=lambda: btnClick("/")).grid(row=4, column=3)

cal.mainloop()
