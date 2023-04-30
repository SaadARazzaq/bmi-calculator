import tkinter as tk

root = tk.Tk()
root.resizable(False, False)
root.configure(bg='cyan')
root.title("BMI Calculator")
root.geometry("600x400")

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height ** 2)
    bmi_label.config(text="Your BMI is: {:.2f}".format(bmi))

    if bmi < 18.5:
        bmi_category_label.config(text="Underweight")
    elif bmi < 25:
        bmi_category_label.config(text="Normal weight")
    elif bmi < 30:
        bmi_category_label.config(text="Overweight")
    elif bmi < 35:
        bmi_category_label.config(text="Obese class I")
    elif bmi < 40:
        bmi_category_label.config(text="Obese class II")
    else:
        bmi_category_label.config(text="Obese class III")

top_label = tk.Label(root, text="BMI Calculator", bg='yellow')
top_label.pack(fill=tk.X)

weight_label = tk.Label(root, text="Enter Your Weight (KGs): ", bg='yellow')
weight_label.pack(pady=(50, 0))

weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Enter Your Height (meters): ", bg='yellow')
height_label.pack(pady=(20, 0))

height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, height=1, width=25, text="CALCULATE", command=calculate_bmi)
calculate_button.pack(pady=(50, 0))

bmi_label = tk.Label(root, text="Your BMI is: ", bg='yellow')
bmi_label.pack()

bmi_category_label = tk.Label(root, text="", bg='yellow')
bmi_category_label.pack()

root.mainloop()
