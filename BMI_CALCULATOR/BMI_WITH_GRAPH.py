from tkinter import *
import matplotlib.pyplot as plt

root = Tk()
root.title("Body Mass Index")
root.geometry("600x400+100+100")

frame1 = Frame(root, pady=10, bd=16)
frame1.grid()

weight = StringVar()
height = StringVar()
result = StringVar()

frame2 = Frame(frame1, width=550, height=190, pady=10, bd=16, relief="sunken")
frame2.grid(row=0, column=0)

frame3 = Frame(frame1, width=550, height=190, pady=10, bd=16, relief="sunken")
frame3.grid(row=1, column=0)

labelweight = Label(frame2, text="Enter Your Weight ", font=("arial", 14, "bold"), bd=12)
labelweight.grid(row=0, column=0, sticky=W)
labelweight = Entry(frame2, textvariable=weight, font=("arial", 14, "bold"), bd=12)
labelweight.grid(row=0, column=1, sticky=W)
labelkg = Label(frame2, text="kg ", font=("arial", 14, "bold"), bd=12)
labelkg.grid(row=0, column=2, sticky=W)

labelheight = Label(frame2, text="Enter Your Height ", font=("arial", 14, "bold"), bd=12)
labelheight.grid(row=1, column=0, sticky=W)
labelheight = Entry(frame2, textvariable=height, font=("arial", 14, "bold"), bd=12)
labelheight.grid(row=1, column=1, sticky=W)
labelmeter = Label(frame2, text="m ", font=("arial", 14, "bold"), bd=12)
labelmeter.grid(row=1, column=2, sticky=W)

labelresult = Label(frame2, text="Show the Result(BMI) ", font=("arial", 14, "bold"), bd=12)
labelresult.grid(row=2, column=0, sticky=W)
labelresult = Entry(frame2, textvariable=result, font=("arial", 14, "bold"), bd=12)
labelresult.grid(row=2, column=1, sticky=W)

def add():
    f = float(weight.get())
    s = float(height.get())  # if we want in centimeter then we have to divide by 100
    a = f / (s * s)
    b = round(a, 2)
    result.set(b)
    show_graph(b)

def Reset():
    weight.set("")
    height.set("")
    result.set("")

def Exit():
    root.destroy()

def show_graph(bmi):
    fig, ax = plt.subplots()
    ax.bar(["BMI"], [bmi], color='blue')
    ax.set_ylim(0, 40)
    ax.set_ylabel("BMI Value")
    ax.set_title("Body Mass Index (BMI) Result")
    plt.axhline(y=18.5, color='green', linestyle='--', label="Underweight")
    plt.axhline(y=24.9, color='yellow', linestyle='--', label="Normal weight")
    plt.axhline(y=29.9, color='orange', linestyle='--', label="Overweight")
    plt.axhline(y=40, color='red', linestyle='--', label="Obesity")
    plt.legend()
    plt.show()

buttonTotal = Button(frame3, text="Total ", font=("arial", 14, "bold"), bd=12, pady=12, width=8, command=add)
buttonTotal.grid(row=0, column=0)
buttonReset = Button(frame3, text="Reset ", font=("arial", 14, "bold"), bd=12, pady=12, width=8, command=Reset)
buttonReset.grid(row=0, column=1)
buttonExit = Button(frame3, text="Exit ", font=("arial", 14, "bold"), bd=12, pady=12, width=8, command=Exit)
buttonExit.grid(row=0, column=2)

root.mainloop()
