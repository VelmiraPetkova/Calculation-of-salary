from tkinter import *
import messagebox
import Self_work

root=Tk()
root.title("salary_document")

label = Label(root, text="Въведете брутната заплата")
label.pack()
gross_salary = Entry(root, bd=5)
gross_salary.pack()

flag=BooleanVar() ##стойността на флага
##flag.set(True)
radioflag0=Radiobutton(root, text="Самоосигуряващ се за тр.злоп. и проф.болест",variable=flag,value=True)
radioflag0.pack(anchor=W)
radioflag1=Radiobutton(root, text="Самоосигуряващ се за всички социални рискове",variable=flag,value=False)
radioflag1.pack(anchor=W)


show=Button(root, text="Изчисли", command=lambda: Self_work.Calculation_net_salary(gross_salary,flag))

show.pack()
root.mainloop()




