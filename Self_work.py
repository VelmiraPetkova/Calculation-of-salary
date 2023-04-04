from tkinter import messagebox

def Calculation_net_salary(gross_salary,flag):
    gross_salary = float(gross_salary.get())
    income_tax_percent=0.1
    pensions_fund_percent=0.05
    additional_pension_insurance_fund_percent=0.08
    flag= bool(flag.get())

    if flag:
        health_insurance_tax_percent=0.148
        health_insurance_tax = health_insurance_tax_percent * gross_salary
    else:
        health_insurance_tax_percent = 0.183
        health_insurance_tax = health_insurance_tax_percent * gross_salary


    pensions_fund= 0.05 * gross_salary
    additional_pension_insurance_fund= 0.08 * gross_salary

    total_tax_ins=pensions_fund+ additional_pension_insurance_fund + health_insurance_tax
    total_tax= gross_salary-total_tax_ins
    income_tax = 0.1 * total_tax

    net_salary=gross_salary-income_tax
    messagebox.showinfo("Нетната заплата е:", f"{net_salary:.2f}")
    exit()
    ##print(f"{net_salary:.2f}")
