import tkinter as tk

root = tk.Tk()
root.title("BMI Health Calculator")


# Function
def calculate_bmi():
    try:
        mass = float(entry_mass.get())
        height_cm = float(entry_height.get())

        height_m = height_cm / 100
        bmi = mass / (height_m ** 2)

        result = f"BMI: {bmi:.2f}"

        # Category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result += f"\nCategory: {category}"

        # Extra message if checkbox checked
        if advice_var.get() == 1:
            result += "\nStay healthy and active!"

        label_result["text"] = result

    except ValueError:
        label_result["text"] = "Enter valid numbers"


# ---- Widgets ----

# Mass
tk.Label(root, text="Mass (kg):").grid(row=0, column=0)
entry_mass = tk.Entry(root)
entry_mass.grid(row=0, column=1)

# Height
# Radiobutton (Gender)
# OptionMenu (Activity)
# Checkbutton
# Button
# Output Label
# Run
